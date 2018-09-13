"""Dad Joke Generator"""

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from api import get_jokes
from markov import make_chains, make_joke
from jinja2 import StrictUndefined

from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()

#Initialize Flask app
app = Flask(__name__)

app.secret_key = "SEEECREEEET"

#Raise an error if there's an undefined variable in Jinja
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage."""
    joke = generate_markov_joke()

    return render_template("index.html", joke=joke)

@app.route('/generate-joke.json')
def generate_markov_joke():
    """Returns a markov chain/new joke."""

    # Check if jokes from API are cached
    jokes = get_dad_jokes()

    # Make Markov chains
    chains = make_chains(jokes)

    # Generate new dad joke
    joke = make_joke(chains)

    # Cache generated markov joke
    cache_markov_jokes(joke)

    return joke

def get_dad_jokes():
    """
    Checks if icanhasdadjoke jokes are stored in a cache. Otherwise, calls API.
    Returns API's jokes.
    """
    jokes = cache.get('dad-jokes')
    if jokes is None:
        #get jokes from icanhazdadjoke API and cache them
        jokes = get_jokes()
        cache.set('dad-jokes', jokes)
    return jokes

def cache_markov_jokes(joke):
    """ Caches generated Markov jokes. """
    jokes = cache.get('markov-jokes')
    if jokes is None:
        cache.set('markov-jokes', [joke])
    else:
        jokes.append(joke)
    return


if __name__ == "__main__":

    # Only start server if all doctests pass
    from doctest import testmod
    if testmod().failed == 0:

    # Use the DebugToolbar
        app.debug = True
        DebugToolbarExtension(app)

        app.run(host="0.0.0.0")