import json
import requests
from variables import link

class points():
    def score_pull(self, uid_data):
        for key in uid_data:
            indi = uid_data[key][0]
            res = requests.get(link + indi)
            scr = res.json()["tus"][0]["p"]
            uid_data[key][1] = scr
        return uid_data
        

