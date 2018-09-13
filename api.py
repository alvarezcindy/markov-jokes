"""Calling the icanhazdadjoke API for jokes"""

import requests, json

def get_jokes():
    """
    """

    dad_jokes = ''

    icanhasdadjoke_url = 'https://icanhazdadjoke.com/search'

    headers = {'User-Agent': 'https://github.com/alvarezcindy', 
               'Accept': 'text/plain'}
 
    for n in range(1,5):
        params = {'current_page': n,
                  'limit': '30'}

        jokes = requests.get(icanhasdadjoke_url, headers=headers, params=params)
        dad_jokes += jokes.text
    
    return dad_jokes