"""Calling the icanhazdadjoke API for jokes"""

import requests, json

def get_jokes():
    icanhasdadjoke_url = 'https://icanhazdadjoke.com/search'

    headers = {'User-Agent': 'https://github.com/alvarezcindy', 
               'Accept': 'application/json'}

    params = {'limit': '30'}

    joke_req = requests.get(icanhasdadjoke_url, headers=headers, params=params)
    jokes = joke_req.json()
    return jokes