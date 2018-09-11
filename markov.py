"""Generate Markov chains from jokes."""
from api import get_jokes
from pprint import pprint
from random import choice

# what happens if you pass in an empty string?
# what happens if you pass in one word?


def make_chains(jokes):
    """
    Takes in jokes as a text string; returns a dictionary of Markov chains.
    Each bigram in the text input is a key and the value is a list of the word(s)
    that follow the bigram in the full text.
    
    >>> jokes = make_chains("knock knock joke")

    >>> sorted(jokes.keys())
    [('knock', 'knock'), ('knock', 'joke')]

    >>> jokes[('knock', 'knock')]
    ['joke']
      
    >>> jokes[('knock','joke')]
    [None]
    """

    words = tuple(jokes.split())

    chains = {}

    for i in range(len(words)-2):
        bigram = words[i:i+2]

        if bigram not in chains:
            chains[bigram] = []

        chains[bigram].append(words[i+2])

    return chains


# def make_joke(chains):

# Get jokes from icanhazdadjoke API
jokes = get_jokes()

# Make Markov chains
chains = make_chains(jokes)

# Generate new dad jokes
dad_jokes = make_joke(chains)
