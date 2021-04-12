import requests
import json

base_url = "https://a.fanzy.in/v5/tournaments/314/compareUsers?fUID="


class scoreInterface:
    def get_latest_tourni_score(self,uid_data):
        for key in uid_data:
            url = base_url+ uid_data[key][0]
            r = requests.get(url)
            info = json.loads(r.text)
            #from here we can get any number of matches data
            uid_data[key][1]= info["tus"][0]['p']