#!/usr/bin/env python
import logging
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

TEAM_ID = 541  # https://dashboard.api-football.com/soccer/ids/teams/Spain

# Init
log = logging.getLogger()
load_dotenv()
API_KEY = os.getenv("API_KEY")
if not os.getenv("API_KEY"):
    log.error("API_KEY environment variable must be defined")
    exit()

# Fetch API
# API doc: https://www.api-football.com/documentation-v3
headers = {"x-rapidapi-host": "v3.football.api-sports.io", "x-rapidapi-key": API_KEY}
url = f"https://v3.football.api-sports.io/fixtures?team={TEAM_ID}&next=5"
response = requests.get(url, headers=headers)
data = response.json()
if data["errors"] == []:
    for match in data["response"]:
        home_team = match["teams"]["home"]["name"]
        away_team = match["teams"]["away"]["name"]
        date = datetime.fromisoformat(match["fixture"]["date"])
        league = f"{match['league']['name']} ({match['league']['country']})"
        print(f"{date.strftime('%Y-%m-%d')}: {home_team} vs {away_team} — {league}")
else:
    print(f"Erreur:\n{data['errors']}")
    exit(-1)
