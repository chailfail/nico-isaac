import os
import requests
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from spotify_user import SpotifyUser

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

client_id = '312a3338244443048ebaea1d463ab3bb'
client_secret = '6dc91bcc6e224d578eb943b890235fc4'
redirect_uri = 'http://localhost:9000'

authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

# https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = ["user-top-read", "user-read-private", "user-read-email"]


def authorize_and_get_token():
    """
    Authorize the user with Spotify and return the access token
    :return: str, the access token from Spotify
    """
    spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
    # Redirect user to Spotify for authorization
    authorization_url, state = spotify.authorization_url(authorization_base_url)
    print('Please go here to authorize: ', authorization_url)

    # Get the authorization verifier code from the callback url
    redirect_response = input('\nPaste the full redirect URL here: ')

    auth = HTTPBasicAuth(client_id, client_secret)

    # Fetch the access token
    token = spotify.fetch_token(token_url, auth=auth, authorization_response=redirect_response)
    return token["access_token"]


def main():
    """
    Main function that authenticates the user and calls methods to print the user's top artists and tracks from Spotify
    """
    access_token = authorize_and_get_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    spotify_api_call = requests.get("https://api.spotify.com/v1/me", headers=headers)
    spotify_json = spotify_api_call.json()
    current_user = SpotifyUser(spotify_json)
    current_user.get_user_top_artists(access_token)
    current_user.get_user_top_tracks(access_token)


main()
