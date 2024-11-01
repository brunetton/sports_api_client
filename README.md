Python command-line interface for https://www.api-football.com API

Usage:
- `API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  ./foot_scrapper.py team [team_id]`
- or using a [env fil](https://dotenvx.com/docs/env-file), simply `./foot_scrapper.py [team_id]`

To find the team ID, goto: https://dashboard.api-football.com/soccer/ids/teams

Example, to list next 10 next matchs for Real Madrid:

    ./foot_scrapper.py team 541

(in results, `W` stands for Women team)
