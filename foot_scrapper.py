#!/usr/bin/env python
import logging
import os
import time
from datetime import datetime

import requests
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

TEAM_ID = 541  # https://allsportsapi.com/soccer-football-api-documentation#Teams
API_DATE_FORMAT = "%Y-%m-%d"

# Init
log = logging.getLogger()
load_dotenv()
API_KEY = os.getenv("API_KEY")
if not os.getenv("API_KEY"):
    log.error("API_KEY environment variable must be defined")
    exit()

# Fetch API
date_after_month = datetime.today() + relativedelta(months=1)
next_month_str = date_after_month.strftime(API_DATE_FORMAT)

# API doc: https://allsportsapi.com/soccer-football-api-documentation
url = f"https://apiv2.allsportsapi.com/football/?met=Fixtures&teamId={TEAM_ID}&from={time.strftime(API_DATE_FORMAT)}&to={next_month_str}&APIkey={API_KEY}"
response = requests.get(url)
data = response.json()
if data["success"] == 1:
    print("Results:")
    for match in data["result"]:
        home_team = match["event_home_team"]
        away_team = match["event_away_team"]
        date = match["event_date"]
        league = match["league_name"]
        print(f"{date}: {home_team} vs {away_team} ({league})")
else:
    print("Erreur")
    exit(-1)
