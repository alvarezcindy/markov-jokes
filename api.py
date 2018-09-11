"""Calling the icanhazdadjoke API for jokes"""

import requests, json

def get_jokes():
    icanhasdadjoke_url = 'https://icanhazdadjoke.com/search'

    headers = {'User-Agent': 'https://github.com/alvarezcindy', 
               'Accept': 'text/plain'}

    params = {'limit': '30'}

    jokes = requests.get(icanhasdadjoke_url, headers=headers, params=params)
    
    return jokes.text