# Markov Dad Jokes

Markov Dad Jokes is a Markov chain generator that uses existing dad jokes to generate new ones. It requests dad jokes as a plain text response from the icanhazdadjoke API to build word patterns. The generated Markov chains are cached. 

## Tech Stack
------

__Frontend:__ Javascript, jQuery, Ajax, Jinja2, Bootstrap, HTML, CSS </br>
__Backend:__ Python, Flask </br>
__APIs:__ icanhazdadjoke API </br>

## Features
------

Users can read generated jokes and click a button to request a new one:
![ScreenShot](/static/img/readme_img1.jpg)

## Installation
------
To run Markov Dad Jokes, please follow the steps below:

Clone repository:
```
$ git clone https://github.com/alvarezcindy/markov-jokes.git
```

Create and activate a virtual environment in the project directory:

```
virtualenv env
source env/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:
```
$ python server.py
```