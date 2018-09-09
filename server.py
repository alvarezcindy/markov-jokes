"""Dad Joke Generator"""

from flask import Flask, render_template, request, flash, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

#Initialize Flask app
app = Flask(__name__)

#Raise an error if there's an undefined variable in Jinja
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage."""
    return render_template("index.html")

if __name__ == "__main__":

    connect_to_db(app)

    # Use the DebugToolbar
    app.debug = True
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")