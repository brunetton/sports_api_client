Python command-line interface for https://www.api-football.com API

## Preparing

- you must get an API key from https://www.api-football.com (it's free)

## Usage:
- `API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  ./foot_scrapper.py team [team_id]`
- or using a [env file](https://dotenvx.com/docs/env-file), simply `./foot_scrapper.py [team_id]`

`.env` file syntax:

```
API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

To list next 10 next matchs for Real Madrid:

    ./foot_scrapper.py team 541

To find the team ID, goto: https://dashboard.api-football.com/soccer/ids/teams (in results, `W` stands for Women team)

## TODO / ideas

- multiple teams support (if you're intersted, open an issue for this feature request)
