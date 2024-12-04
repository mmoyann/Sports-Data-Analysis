from src.live_data import fetch_live_nba_games, process_live_game_data, display_live_games, plot_live_scores

if __name__ == "__main__":
    API_KEY = "41b96d1876mshba52a30b0b754d0p14715ejsn156ee05f47c3"  # Replace with your actual API key

    # Fetch live NBA games
    live_games_df = fetch_live_nba_games(API_KEY)

    # Process the data
    processed_live_games = process_live_game_data(live_games_df)

    # Display live games
    display_live_games(processed_live_games)

    # Plot live scores
    plot_live_scores(processed_live_games)
