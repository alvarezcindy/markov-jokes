import server
from unittest import TestCase

class MarkovDadJokesTest(TestCase):
    """Tests for Markov Dad Jokes site."""

    def set_up(self):
        """Will run befor every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_index(self):
        """Checks if the homepage can be reached."""

        result = client.get('/')
        self.assertIn(b'Another Joke!', result.data)

    def test_joke_generator(self):
        """Checks if route "/generate-joke.json' is successful."""

        result = self.client.get("/generate-joke.json")
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()