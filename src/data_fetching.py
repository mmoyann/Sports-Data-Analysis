from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

import pandas as pd

def get_all_teams():
    """
    Retrieves all NBA teams and their details.
    """
    teams_list = teams.get_teams()
    return pd.DataFrame(teams_list)

# Example usage:
nba_teams = get_all_teams()
print(nba_teams[['full_name', 'id']])  # View team names and IDs


def get_team_game_log(team_id, season='2023-24'):
    """
    Fetches the game logs for a specific team.
    """
    logs = teamgamelog.TeamGameLog(team_id=team_id, season=season).get_data_frames()[0]
    return logs


def get_all_players():
    """
    Retrieves all NBA players and their details.
    """
    players_list = players.get_players()
    return pd.DataFrame(players_list)

nba_players = get_all_players()


def get_player_game_logs(player_id, season='2023-24'):
    """
    Fetches game logs for a specific player in a given season.
    """
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season).get_data_frames()[0]
    return game_log

def fetch_and_save_team_data(team_name, season='2023-24'):
    team_id = nba_teams[nba_teams['full_name'] == team_name]['id'].values[0]
    team_logs = get_team_game_log(team_id, season)
    team_logs.to_csv(f'data/{team_name.replace(" ", "_").lower()}_game_logs.csv', index=False)
    print(f"{team_name} data saved!")

def fetch_and_save_player_data(player_name, season='2023-24'):
    player_id = nba_players[nba_players['full_name'] == player_name]['id'].values[0]
    player_logs = get_player_game_logs(player_id, season)
    player_logs.to_csv(f'data/{player_name.replace(" ", "_").lower()}_game_logs.csv', index=False)
    print(f"{player_name} data saved!")

# Fetch and save data for teams and players
fetch_and_save_team_data('Los Angeles Lakers')
fetch_and_save_player_data('LeBron James')
