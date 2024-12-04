import src.betting_logic
print(dir(src.betting_logic))

from src.betting_logic import identify_value_bets, display_recommendations

from src.live_data import fetch_live_nba_games, process_live_game_data, display_live_games, plot_live_scores
from src.sportsbet_odds_process import process_odds_data, calculate_implied_probability
from src.betting_logic import identify_value_bets, display_recommendations
import requests

if __name__ == "__main__":
    API_KEY = "77af32eee05ae50c0d81fe32b24d892a"  

    # Fetch live NBA games
    live_games_df = fetch_live_nba_games(API_KEY)
    processed_live_games = process_live_game_data(live_games_df)
    display_live_games(processed_live_games)
    plot_live_scores(processed_live_games)

    # Fetch NBA odds
    print("\nFetching NBA odds...")
    odds_response = requests.get(
        "https://api.the-odds-api.com/v4/sports/basketball_nba/odds",
        params={
            "api_key": API_KEY,
            "regions": "au",
            "markets": "h2h,spreads",
            "oddsFormat": "decimal",
            "dateFormat": "iso",
        }
    )

    if odds_response.status_code != 200:
        print(f"Failed to fetch odds: {odds_response.status_code}")
    else:
        odds_json = odds_response.json()

        # Process odds data
        odds_df = process_odds_data(odds_json)
        odds_df['implied_probability'] = odds_df['odds'].apply(calculate_implied_probability)
        print(odds_df.head())

        # Example model predictions (replace with actual model outputs)
        predictions = {'Los Angeles Lakers': 0.6, 'Golden State Warriors': 0.4}

        # Identify value bets
        value_bets = identify_value_bets(odds_df, predictions)

        # Display recommendations
        display_recommendations(value_bets)
