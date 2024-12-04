import pandas as pd

def process_odds_data(odds_json):
    """
    Processes the odds data into a structured DataFrame.
    """
    data = []
    for event in odds_json:
        home_team = event['home_team']
        away_team = event['away_team']
        for bookmaker in event['bookmakers']:
            bookmaker_name = bookmaker['title']
            for market in bookmaker['markets']:
                market_type = market['key']
                for outcome in market['outcomes']:
                    data.append({
                        'home_team': home_team,
                        'away_team': away_team,
                        'bookmaker': bookmaker_name,
                        'market_type': market_type,
                        'outcome_name': outcome['name'],
                        'odds': outcome['price']
                    })
    return pd.DataFrame(data)

def calculate_implied_probability(odds):
    """
    Converts decimal betting odds into implied probabilities.
    """
    return 1 / odds
