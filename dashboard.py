from dash import Dash, dcc, html, dash_table
import plotly.express as px
import pandas as pd
from src.betting_logic import identify_value_bets
from src.sportsbet_odds_process import process_odds_data, calculate_implied_probability

API_KEY = "77af32eee05ae50c0d81fe32b24d892a"

# Fetch and process odds
def fetch_and_process_odds():
    import requests
    odds_response = requests.get(
        "https://api.the-odds-api.com/v4/sports/basketball_nba/odds",
        params={
            "api_key": API_KEY,
            "regions": "us",
            "markets": "h2h,spreads",
            "oddsFormat": "decimal",
            "dateFormat": "iso",
        }
    )

    if odds_response.status_code != 200:
        return pd.DataFrame()

    odds_json = odds_response.json()
    odds_df = process_odds_data(odds_json)
    odds_df['implied_probability'] = odds_df['odds'].apply(calculate_implied_probability)
    return odds_df

# Dash App
app = Dash(__name__)
odds_df = fetch_and_process_odds()

# Example model predictions
predictions = {'Los Angeles Lakers': 0.6, 'Golden State Warriors': 0.4}
value_bets = identify_value_bets(odds_df, predictions)

# App Layout
app.layout = html.Div([
    html.H1("NBA Betting Dashboard"),
    
    # Display Odds Data
    html.H2("NBA Odds"),
    dash_table.DataTable(
        data=odds_df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in odds_df.columns],
        style_table={'overflowX': 'auto'}
    ),

    # Display Value Bets
    html.H2("Value Bets"),
    dash_table.DataTable(
        data=value_bets.to_dict('records'),
        columns=[{"name": i, "id": i} for i in value_bets.columns],
        style_table={'overflowX': 'auto'}
    ),

    # Value Bets Visualization
    html.H2("Value Bets Visualization"),
    dcc.Graph(
        figure=px.bar(
            value_bets,
            x='team',
            y='value',
            title="Value Bets (Positive Expected Value)",
            labels={'value': 'Value (Model Probability - Implied Probability)'}
        )
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
