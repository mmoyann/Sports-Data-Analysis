from nba_api.stats.endpoints import teamgamelog, playergamelog, teamplayerdashboard
from nba_api.stats.static import teams, players
import pandas as pd
import os

# Ensure the 'data/' directory exists
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Fetch all teams
def get_all_teams():
    """
    Retrieves all NBA teams and their details.
    """
    teams_list = teams.get_teams()
    return pd.DataFrame(teams_list)

nba_teams = get_all_teams()


# Fetch game logs for a specific team
def get_team_game_log(team_id, season='2023-24'):
    """
    Fetches the game logs for a specific NBA team by team ID.
    """
    try:
        logs = teamgamelog.TeamGameLog(team_id=team_id, season=season).get_data_frames()[0]
        return logs
    except Exception as e:
        print(f"Error fetching game logs for team ID {team_id}: {e}")
        return pd.DataFrame()

# Fetch all players
def get_all_players():
    """
    Retrieves all NBA players and their details.
    """
    players_list = players.get_players()
    return pd.DataFrame(players_list)

nba_players = get_all_players()

# Fetch game logs for a specific player
def get_player_game_logs(player_id, season='2023-24'):
    """
    Fetches game logs for a specific NBA player by player ID.
    """
    try:
        game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season).get_data_frames()[0]
        return game_log
    except Exception as e:
        print(f"Error fetching game logs for player ID {player_id}: {e}")
        return pd.DataFrame()

# Fetch and save game logs for all teams
def fetch_all_teams_data(season='2023-24'):
    """
    Fetches game logs for all NBA teams and saves them to CSV files.
    """
    for _, team in nba_teams.iterrows():
        team_name = team['full_name']
        team_id = team['id']
        try:
            team_logs = get_team_game_log(team_id, season)
            if not team_logs.empty:
                file_path = os.path.join(DATA_DIR, f"{team_name.replace(' ', '_').lower()}_game_logs.csv")
                team_logs.to_csv(file_path, index=False)
                print(f"Data saved for {team_name} to {file_path}")
            else:
                print(f"No game logs found for {team_name} in the {season} season.")
        except Exception as e:
            print(f"Error fetching data for {team_name}: {e}")

# Fetch and save player data for a specific team
def fetch_team_players(team_id, season='2023-24'):
    """
    Fetches all players' game data for a specific team.
    """
    try:
        data = teamplayerdashboard.TeamPlayerDashboard(team_id=team_id, season=season).get_data_frames()[1]
        return data
    except Exception as e:
        print(f"Error fetching team players for Team ID {team_id}: {e}")
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    print("Fetching all teams' data...")
    fetch_all_teams_data()

