import server
import unittest

class MarkovDadJokesTest(unittest.TestCase):
    """Tests for Markov Dad Jokes site."""

    def setUp(self):
        """Will run before every test."""

        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_index(self):
        """Checks if the homepage can be reached."""

        result = self.client.get('/')
        self.assertIn(b'Another Joke!', result.data)

    def test_joke_generator(self):
        """Checks if route "/generate-joke.json' is successful."""

        result = self.client.get('/generate-joke.json')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()