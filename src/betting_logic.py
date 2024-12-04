
import pandas as pd


def identify_value_bets(odds_df, predictions):
    """
    Identifies value bets by comparing implied probabilities with model predictions.
    """
    value_bets = []
    for _, row in odds_df.iterrows():
        team = row['outcome_name']
        implied_prob = row['implied_probability']
        model_prob = predictions.get(team, 0)  # Model's probability for the team

        if model_prob > implied_prob:
            value_bets.append({
                'team': team,
                'odds': row['odds'],
                'implied_probability': implied_prob,
                'model_probability': model_prob,
                'value': model_prob - implied_prob
            })

    return pd.DataFrame(value_bets)

def display_recommendations(value_bets):
    """
    Displays value betting recommendations in a clear table format.
    """
    if value_bets.empty:
        print("No value bets found.")
        return

    print("\nRecommended Bets:")
    print(value_bets[['team', 'odds', 'implied_probability', 'model_probability', 'value']])
