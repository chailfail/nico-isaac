import requests


class SpotifyUser:
    def __init__(self, spotify_json):
        self.display_name = spotify_json["display_name"]

    def get_user_top_artists(self, access_token):
        """
        Fetch and print the user's top artists from Spotify
        :param access_token: str, the access token from Spotify
        """
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        spotify_api_call = requests.get("https://api.spotify.com/v1/me/top/artists?limit=10&offset=0", headers=headers)
        spotify_json = spotify_api_call.json()
        top_artists_list = []
        for item in spotify_json["items"]:
            top_artists_list.append(item["name"])
        print("\n{}'s top artists:".format(self.display_name))
        for artist in top_artists_list:
            print(artist)
        return top_artists_list

    def get_user_top_tracks(self, access_token):
        """
        Fetch and print the user's top tracks from Spotify
        :param access_token: str, the access token from Spotify
        """
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        spotify_api_call = requests.get("https://api.spotify.com/v1/me/top/tracks?limit=10&offset=0", headers=headers)
        spotify_json = spotify_api_call.json()
        top_tracks_list = []
        for item in spotify_json["items"]:
            top_tracks_list.append(item["name"])
        print("\n{}'s top tracks:".format(self.display_name))
        for track in top_tracks_list:
            print(track)
        return top_tracks_list
