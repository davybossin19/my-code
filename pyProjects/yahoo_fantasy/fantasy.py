from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

CUR_LEAGUE = "414.l.1107622"

def get_players_team(league: yfa.League, player_id: int) -> str:
    ownership_dict = league.ownership([player_id])
    player = ownership_dict[str(player_id)]
    return player['owner_team_name']

def print_all_rosters(league: yfa.League, team_ids: list[dict]):
    percent_owned_map = get_percent_owned_dict(league)

    for team_id in team_ids.keys():
        print(team_ids[team_id]['name'])
        count = 0
        percent_owned_tally = 0
        for player in league.to_team(team_id).roster():
            print("{} - {}".format(player['name'], player['eligible_positions'][0]))
            count += 1
            percent_owned_tally += percent_owned_map[player['player_id']]
        print("Average Percent Owned: {}".format(round(percent_owned_tally/count, 2)))
        print("------END OF TEAM-------")

def rank_teams_by_unweighted_percent_owned(league: yfa.League, team_ids: list[dict[str, int]]):
    percent_owned_map = get_percent_owned_dict(league)

    unsorted_teams = []

    for team_id in team_ids.keys():
        
        count = 0
        percent_owned_tally = 0

        for player in league.to_team(team_id).roster():
            count += 1
            percent_owned_tally += percent_owned_map[player['player_id']]

        name_perc_map = {'name': team_ids[team_id]['name'], 'avg': percent_owned_tally / count }
        unsorted_teams.append(name_perc_map)

    sorted_teams = sorted(unsorted_teams, key=lambda x: x['avg'], reverse=True)
    return sorted_teams

        

def get_percent_owned_dict(league: yfa.League) -> dict[int, int]:
    players = league.taken_players()

    percent_owned_dict={}

    for player in players:
        percent_owned_dict[player['player_id']] = player['percent_owned']

    return percent_owned_dict

def main():
    sc = OAuth2(None, None, from_file="oauth.json")

    gm = yfa.Game(sc, 'nfl')

    leagues = gm.league_ids()

    print('-'*10)

    lg = gm.to_league(CUR_LEAGUE)

    team_ids = lg.teams()


    print_all_rosters(lg, team_ids)
    sorted_teams = rank_teams_by_unweighted_percent_owned(lg, team_ids)
    
    for i, team in enumerate(sorted_teams):
        print("{} - {} - Average Ownership %: {}".format(i + 1, team['name'], round(team['avg'], 2)))

if __name__ == "__main__":
    main()