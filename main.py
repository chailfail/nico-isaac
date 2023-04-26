import requests


class SpotifyUserData:
    def __init__(self, user_json):
        self.top_artists_list = user_json["items"][0]["name"]


def main():
    client_id = "312a3338244443048ebaea1d463ab3bb"
    authorization_call = requests.get("https://accounts.spotify.com/authorize?client_id={}&response_type=code"
                                      "&redirect_uri=http://localhost:9000".format(client_id))
    spotify_api_call = requests.get("https://api.spotify.com/v1/me/top/artists?limit=10&offset=0")
    spotify_json = spotify_api_call.json()
    spotify_data = SpotifyUserData(spotify_json)
    user_top_artists = spotify_data.top_artists_list
    print(user_top_artists)


main()
