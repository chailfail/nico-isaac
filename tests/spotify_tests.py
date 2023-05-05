import json
import requests
import unittest
from spotify_library import authorize_and_get_token

access_token = authorize_and_get_token()
headers = {
    "Authorization": f"Bearer {access_token}"
}


class SpotifyUserTests(unittest.TestCase):

    def test_me_spotify_json(self):
        with open("nico_me_spotify.json", 'r') as spotify_input_file:
            nico_me_spotify_json = json.load(spotify_input_file)
        spotify_api_call = requests.get("https://api.spotify.com/v1/me", headers=headers)
        api_spotify_json = spotify_api_call.json()
        self.assertEqual(nico_me_spotify_json["display_name"], api_spotify_json["display_name"])
        self.assertTrue("id" in api_spotify_json)
        self.assertIsInstance(api_spotify_json["id"], str)
        self.assertTrue("email" in api_spotify_json)
        self.assertIsInstance(api_spotify_json["email"], str)
        self.assertTrue("country" in api_spotify_json)
        self.assertIsInstance(api_spotify_json["country"], str)
        self.assertTrue("product" in api_spotify_json)
        self.assertIsInstance(api_spotify_json["product"], str)

    def test_artists_spotify_json(self):
        spotify_api_call = requests.get("https://api.spotify.com/v1/me/top/artists?limit=10&offset=0", headers=headers)
        api_spotify_json = spotify_api_call.json()
        self.assertTrue("items" in api_spotify_json)
        self.assertTrue(len(api_spotify_json["items"]) <= 10)
        for artist in api_spotify_json["items"]:
            self.assertTrue("id" in artist)
            self.assertTrue("name" in artist)

    def test_tracks_spotify_json(self):
        spotify_api_call = requests.get("https://api.spotify.com/v1/me/top/tracks?limit=10&offset=0", headers=headers)
        api_spotify_json = spotify_api_call.json()
        self.assertTrue("items" in api_spotify_json)
        self.assertTrue(len(api_spotify_json["items"]) <= 10)
        for track in api_spotify_json["items"]:
            self.assertTrue("id" in track)
            self.assertTrue("name" in track)


if __name__ == '__main__':
    unittest.main()
