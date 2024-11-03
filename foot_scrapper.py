#!/usr/bin/env python

"""
Display next matchs of given team.
To get the team id: https://dashboard.api-football.com/soccer/ids/teams/

Usage:
    {self_filename} team <team_id> [options]
    {self_filename} -h | --help

Options:
    -n --number <number>         Number of matchs to get [default: 10]
    --dump                       Dump full json response (for debugging purpose)
"""

import json
import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import pytz
import requests
from docopt import docopt
from dotenv import load_dotenv
from tzlocal import get_localzone

# Init
log = logging.getLogger()
logging.basicConfig(level=logging.INFO, format="%(message)s")
args = docopt(__doc__.format(self_filename=Path(__file__).name))
load_dotenv()
API_KEY = os.getenv("API_KEY")
if not os.getenv("API_KEY"):
    log.error("API_KEY environment variable must be defined")
    exit()

# Fetch API
# API doc: https://www.api-football.com/documentation-v3
headers = {"x-rapidapi-host": "v3.football.api-sports.io", "x-rapidapi-key": API_KEY}
url = f"https://v3.football.api-sports.io/fixtures?team={args['<team_id>']}&next={args['--number']}"
response = requests.get(url, headers=headers)
data = response.json()
if args["--dump"]:
    json.dump(data, sys.stdout, indent=2)
    exit()
if data["errors"] == []:
    for match in data["response"]:
        try:
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            date = datetime.fromisoformat(match["fixture"]["date"])
            # Make date "aware" of current timezone
            utc_date = date.replace(tzinfo=pytz.UTC)
            local_date = utc_date.astimezone(get_localzone())

            round = match["league"].get("round")
            if round:
                # extract round number from round name. Ex: "Regular Season - 16" -> "16"
                re_match = re.search("(\d+)", round)
                if re_match:
                    round_str = f" - round {re_match.group(0)}"
            league = f"{match['league']['name']} ({match['league']['country']}){round_str}"
            print(f"{local_date.strftime('%a %Y-%m-%d %H:%M')}: {home_team} vs {away_team} — {league}")
        except Exception as e:
            log.info(match)
            raise e
else:
    print(f"Erreur:\n{data['errors']}")
    exit(-1)
