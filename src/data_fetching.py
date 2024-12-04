from nba_api.stats.endpoints import teamgamelog

def get_team_game_log(team_id, season='2023-24'):
    """
    Fetches the game logs for a specific team.
    """
    logs = teamgamelog.TeamGameLog(team_id=team_id, season=season).get_data_frames()[0]
    return logs