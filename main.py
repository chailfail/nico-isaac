import os
import requests
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

client_id = '312a3338244443048ebaea1d463ab3bb'
client_secret = '6dc91bcc6e224d578eb943b890235fc4'
redirect_uri = 'http://localhost:9000'

authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

# https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = ["user-top-read"]


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


def user_top_artists(access_token):
    """
    Fetch and print the user's top artists from Spotify
    :param access_token: str, the access token from Spotify
    """
    # Set the header with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    spotify_api_call = requests.get("https://api.spotify.com/v1/me/top/artists?limit=10&offset=0", headers=headers)
    spotify_json = spotify_api_call.json()
    top_artists_list = []
    for item in spotify_json["items"]:
        top_artists_list.append(item["name"])
    print("\nUser's top artists:")
    for artist in top_artists_list:
        print(artist)


def user_top_tracks(access_token):
    """
    Fetch and print the user's top tracks from Spotify
    :param access_token: str, the access token from Spotify
    """
    # Set the header with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    spotify_api_call = requests.get("https://api.spotify.com/v1/me/top/tracks?limit=10&offset=0", headers=headers)
    spotify_json = spotify_api_call.json()
    top_tracks_list = []
    for item in spotify_json["items"]:
        top_tracks_list.append(item["name"])
    print("\nUser's top tracks:")
    for track in top_tracks_list:
        print(track)


def main():
    """
    Main function that authenticates the user, fetches, and prints the user's top artists and tracks from Spotify
    """
    access_token = authorize_and_get_token()
    user_top_artists(access_token)
    user_top_tracks(access_token)


main()
