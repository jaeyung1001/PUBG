from collections import defaultdict

import json
import requests
import pandas as pd

class PUBG:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        PUBG.header = {
            "Authorization": "Bearer " + self.API_KEY,
            "accept": "application/vnd.api+json"
        }

        PUBG.game_mode_list = ['solo', 'solo-fpp',
                         'duo', 'duo-fpp',
                         'squad', 'squad-fpp']

    def Lifetime(self, user_name, game_mode):
        game_mode_list = ['solo', 'solo-fpp',
                         'duo', 'duo-fpp',
                         'squad', 'squad-fpp']
        self.game_mode = game_mode
        if not self.game_mode in PUBG.game_mode_list:
            print("Invalid Game Mode!")
            print("Game mode list: [solo, solo-fpp, duo, duo-fpp, squad, squad-fpp]")
            
        else:
            self.user_name = user_name
            url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=" + self.user_name
            r = requests.get(url, headers=PUBG.header)
            user_id = r.json()['data'][0]['id']
            url = "https://api.pubg.com/shards/steam/players/"+ user_id +"/seasons/lifetime"
            r = requests.get(url, headers=PUBG.header)
            return r.json()['data']['attributes']['gameModeStats'][self.game_mode]
    
    def Players(self, user_name):
        self.user_name = user_name
        url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=" + self.user_name
        r = requests.get(url, headers=PUBG.header)
        return r.json()
    
    def LeaderBoards(self, game_mode, sort_target='rank'):
        leader_pd = pd.DataFrame(columns=['name', 'rank', 'averagedamage', 'averagerank',
                                         'play_games', 'kd', 'kill', 'rankpoints',
                                         'winratio', 'win_times'])

        self.game_mode = game_mode
        if not self.game_mode in PUBG.game_mode_list:
            print("Invalid Game Mode!")
            print("Game mode list: [solo, solo-fpp, duo, duo-fpp, squad, squad-fpp]")
            
        else:
            url = "https://api.pubg.com/shards/steam/leaderboards/" + self.game_mode
            r = requests.get(url, headers = PUBG.header)
            
            for data in r.json()['included']:
                attributes = data['attributes']
                stats = attributes['stats']
                leader_pd = leader_pd.append({'name':attributes['name'],
                                              'rank': attributes['rank'],
                                              'averagedamage': stats['averageDamage'],
                                              'averagerank': stats['averageRank'],
                                              'playgames': stats['games'],
                                              'kd': stats['killDeathRatio'],
                                              'kill': stats['kills'],
                                              'rankpoints': stats['rankPoints'],
                                              'winratio': stats['winRatio'],
                                              'wintimes': stats['wins']}, ignore_index=True)
            sort_target = sort_target.lower()
            if not sort_target == 'rank':
            	return leader_pd.sort_values(by=[sort_target], ascending=False)
            else:
            	return leader_pd.sort_values(by=[sort_target])

    def season_stats(self, user_name, game_mode):
        self.user_name = user_name
        self.game_mode = game_mode.lower()
        if not self.game_mode in PUBG.game_mode_list:
            print("Invalid Game Mode!")
            print("Game mode list: [solo, solo-fpp, duo, duo-fpp, squad, squad-fpp]")
            
        else:
            url = "https://api.pubg.com/shards/steam/players?filter[playerNames]=" + self.user_name
            r = requests.get(url, headers = PUBG.header)
            user_id = r.json()['data'][0]['id']
            url = "https://api.pubg.com/shards/steam/players/%s/seasons/division.bro.official.pc-2018-01" % user_id
            r = requests.get(url, headers = PUBG.header)
            return r.json()['data']['attributes']['gameModeStats'][self.game_mode]

    # def new_function(self): 