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

    words = jokes.split()

    chains = {}

    for i in range(len(words)-2):
        bigram = tuple(words[i:i+2])

        if bigram not in chains:
            chains[bigram] = []

        chains[bigram].append(words[i+2])

    return chains


def make_joke(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = list(key)

    while key in chains:
        key_string = len(str(words))
        if key_string >= 200:
            break
        new = choice(chains[key])
        words.append(new)
        key = key[1:] + (new,)

    for i in reversed(range(len(words))):
        if words[i][-1] in '!.-"':
            words = words[:i+1]
            break

    words[0] = words[0].capitalize()

    return " ".join(words)
