import unittest
from main import *


class SpotifyTests(unittest.TestCase):
    def test_user_top_artists(self):
        self.assertEqual(user_top_artists(), False)


if __name__ == '__main__':
    unittest.main()
