import requests
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


# Credentials you get from registering a new application
client_id = '312a3338244443048ebaea1d463ab3bb'
client_secret = '6dc91bcc6e224d578eb943b890235fc4'
redirect_uri = 'http://localhost:9000'

# OAuth endpoints given in the Spotify API documentation
# https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
# https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = ["user-read-email", "playlist-read-collaborative", "user-top-read"]

spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

# Redirect user to Spotify for authorization
authorization_url, state = spotify.authorization_url(authorization_base_url)
print('Please go here and authorize: ', authorization_url)

# Get the authorization verifier code from the callback url
redirect_response = input('\n\nPaste the full redirect URL here: ')

auth = HTTPBasicAuth(client_id, client_secret)

# Fetch the access token
token = spotify.fetch_token(token_url, auth=auth, authorization_response=redirect_response)

print(token)

# Fetch a protected resource, i.e. user profile
r = spotify.get('https://api.spotify.com/v1/me')
print(r.content)







class SpotifyUserData:
    def __init__(self, user_json):
        top_artists_list = []
        for item in user_json["items"]:
            top_artists_list.append(item["name"])
        self.top_artists_list = top_artists_list


def main():
    access_token = token["access_token"]

    # Set the header with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    spotify_api_call = requests.get("https://api.spotify.com/v1/me/top/artists?limit=10&offset=0", headers=headers)
    print("Status code:", spotify_api_call.status_code)
    print("Response content:", spotify_api_call.content)

    try:
        spotify_json = spotify_api_call.json()
    except Exception as e:
        print(f"Error decoding JSON: {e}")
        return
    spotify_json = spotify_api_call.json()
    print(spotify_json)
    print(spotify_json)
    print(spotify_json["items"])
    spotify_data = SpotifyUserData(spotify_json)
    user_top_artists = spotify_data.top_artists_list
    print(user_top_artists)
    print("\n\n")
    print("User's top artists:")
    for artist in user_top_artists:
        print(artist)


main()
