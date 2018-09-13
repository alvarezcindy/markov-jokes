"""Calling the icanhazdadjoke API for jokes"""

import requests

def get_jokes():
    """ Calls icanhazdadjoke API. Returns jokes as text/string."""

    dad_jokes = ''

    icanhasdadjoke_url = 'https://icanhazdadjoke.com/search'
    headers = {'User-Agent': 'https://github.com/alvarezcindy', 
               'Accept': 'text/plain'}

    # Calls 4 pages of results
    for n in range(1,5):
        params = {'current_page': n,
                  'limit': '30'}

        jokes = requests.get(icanhasdadjoke_url, headers=headers, params=params)
        dad_jokes += jokes.text
    
    return dad_jokes