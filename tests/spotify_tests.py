import unittest
import requests
from spotify_user import SpotifyUser
from main import authorize_and_get_token

access_token = authorize_and_get_token()
headers = {
    "Authorization": f"Bearer {access_token}"
}
spotify_api_call = requests.get("https://api.spotify.com/v1/me", headers=headers)
spotify_json = spotify_api_call.json()
current_user = SpotifyUser(spotify_json)
test_user = SpotifyUser(spotify_json)


class SpotifyUserTests(unittest.TestCase):

    def test_user_top_artists(self):
        self.assertEqual(test_user.get_user_top_artists(access_token), [])

    def test_user_top_tracks(self):
        self.assertEqual(test_user.get_user_top_tracks(access_token), [])


if __name__ == '__main__':
    unittest.main()
