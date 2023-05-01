import requests
from random import randint
from spotify_user import SpotifyUser
from spotify_library import authorize_and_get_token
from genius_lyrics_library import Song, GuessingGames


# The main file that will combine the Spotify and Genius APIs


def main():
    access_token = authorize_and_get_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    spotify_api_call = requests.get("https://api.spotify.com/v1/me", headers=headers)
    spotify_json = spotify_api_call.json()
    current_user = SpotifyUser(spotify_json)
    user_top_artists = current_user.get_user_top_artists(access_token)
    print(user_top_artists)
    user_top_tracks = current_user.get_user_top_tracks(access_token)
    random_artist = user_top_artists[(randint(0, 9))]

    current_song = Song(random_artist)
    current_game = GuessingGames(current_song)
    # current_game.easy()
    current_game.medium()
    # current_game.hard()


main()
