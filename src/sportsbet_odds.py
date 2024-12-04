import requests

# API Key from Odds API
API_KEY = '77af32eee05ae50c0d81fe32b24d892a'

def fetch_sports(api_key):
    """
    Fetches a list of in-season sports.
    """
    response = requests.get(
        'https://api.the-odds-api.com/v4/sports',
        params={'api_key': api_key}
    )

    if response.status_code != 200:
        print(f"Failed to fetch sports: {response.status_code}")
        return None
    return response.json()

sports = fetch_sports(API_KEY)
for sport in sports:
    print(f"Sport: {sport['title']}, Key: {sport['key']}")

# Look for 'basketball_nba' in the output

def fetch_nba_odds(api_key, sport_key, regions='us', markets='h2h,spreads', odds_format='decimal', date_format='iso'):
    """
    Fetches live and upcoming NBA games along with odds.
    """
    response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/{sport_key}/odds',
        params={
            'api_key': api_key,
            'regions': regions,
            'markets': markets,
            'oddsFormat': odds_format,
            'dateFormat': date_format,
        }
    )

    if response.status_code != 200:
        print(f"Failed to fetch odds: {response.status_code}")
        return None

    print(f"Remaining requests: {response.headers.get('x-requests-remaining')}")
    return response.json()

nba_odds = fetch_nba_odds(API_KEY, 'basketball_nba')
print("Number of events:", len(nba_odds))
for event in nba_odds:
    print(f"Matchup: {event['home_team']} vs {event['away_team']}")
    print("Bookmakers:")
    for bookmaker in event['bookmakers']:
        print(f" - {bookmaker['title']}")
        for market in bookmaker['markets']:
            print(f"   Market: {market['key']}")
            for outcome in market['outcomes']:
                print(f"     {outcome['name']}: {outcome['price']}")
