import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch live NBA games
def fetch_live_nba_games(api_key):
    url = "https://api-nba-v1.p.rapidapi.com/games/live/"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        live_data = response.json()
        if live_data['response']:
            return pd.DataFrame(live_data['response'])
        else:
            print("No live games at the moment.")
            return pd.DataFrame()
    else:
        print(f"Error: {response.status_code}")
        return pd.DataFrame()

# Process the live game data
def process_live_game_data(live_games_df):
    if live_games_df.empty:
        print("No live games to process.")
        return None

    live_games_df = live_games_df[['id', 'teams', 'scores', 'status']]
    processed_games = []
    for _, game in live_games_df.iterrows():
        game_info = {
            "Game ID": game['id'],
            "Home Team": game['teams']['home']['name'],
            "Away Team": game['teams']['visitors']['name'],
            "Home Score": game['scores']['home']['points'],
            "Away Score": game['scores']['visitors']['points'],
            "Status": game['status']['long']
        }
        processed_games.append(game_info)
    return pd.DataFrame(processed_games)

# Display live games
def display_live_games(processed_df):
    if processed_df is not None and not processed_df.empty:
        print("\nLive NBA Games:")
        print(processed_df.to_string(index=False))
    else:
        print("No live games currently.")

# Plot live scores
def plot_live_scores(processed_df):
    if processed_df is None or processed_df.empty:
        print("No data to visualize.")
        return

    plt.figure(figsize=(10, 6))
    plt.bar(processed_df['Home Team'], processed_df['Home Score'], label='Home Team', alpha=0.7)
    plt.bar(processed_df['Away Team'], processed_df['Away Score'], label='Away Team', alpha=0.7)
    plt.title("Live NBA Game Scores")
    plt.xlabel("Teams")
    plt.ylabel("Scores")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
