from nba_api.stats.endpoints import teamgamelog, playergamelog
from nba_api.stats.static import teams, players
import pandas as pd
import os

# Ensure the 'data/' directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Fetch all teams
def get_all_teams():
    teams_list = teams.get_teams()
    return pd.DataFrame(teams_list)

nba_teams = get_all_teams()
print(nba_teams[['full_name', 'id']])  # View team names and IDs

# Fetch game logs for a specific team
def get_team_game_log(team_id, season='2023-24'):
    logs = teamgamelog.TeamGameLog(team_id=team_id, season=season).get_data_frames()[0]
    return logs

# Fetch all players
def get_all_players():
    players_list = players.get_players()
    return pd.DataFrame(players_list)

nba_players = get_all_players()

# Fetch game logs for a specific player
def get_player_game_logs(player_id, season='2023-24'):
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season).get_data_frames()[0]
    return game_log


def fetch_all_teams_data(season='2023-24'):
    """
    Fetches game logs for all NBA teams and saves them to CSV files.
    """
    for _, team in nba_teams.iterrows():
        team_name = team['full_name']
        team_id = team['id']
        try:
            team_logs = get_team_game_log(team_id, season)
            team_logs.to_csv(f'data/{team_name.replace(" ", "_").lower()}_game_logs.csv', index=False)
            print(f"Data saved for {team_name}")
        except Exception as e:
            print(f"Error fetching data for {team_name}: {e}")

fetch_all_teams_data()

def fetch_all_players_data(season='2023-24'):
    """
    Fetches game logs for all NBA players and saves them to CSV files.
    """
    for _, player in nba_players.iterrows():
        player_name = player['full_name']
        player_id = player['id']
        try:
            player_logs = get_player_game_logs(player_id, season)
            player_logs.to_csv(f'data/{player_name.replace(" ", "_").lower()}_game_logs.csv', index=False)
            print(f"Data saved for {player_name}")
        except Exception as e:
            print(f"Error fetching data for {player_name}: {e}")

fetch_all_players_data()
 
