import requests
from random import randint
from spotify_user import SpotifyUser
from spotify_library import authorize_and_get_token
from genius_lyrics_library import Song, GuessingGames

artist_ids = {
    "Jons": 1055422,
}


# note: The Beatles sometimes raises a TimeoutError, not sure why
def main():
    access_token = authorize_and_get_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    spotify_api_call = requests.get("https://api.spotify.com/v1/me", headers=headers)
    spotify_json = spotify_api_call.json()
    current_user = SpotifyUser(spotify_json)
    user_top_artists = current_user.get_user_top_artists(access_token)
    user_top_tracks = current_user.get_user_top_tracks(access_token)
    random_artist = user_top_artists[randint(0, 9)]
    # random_artist = user_top_artists[2]
    # ^ to test a specific artist
    artist_id = artist_ids.get(random_artist)
    print()
    current_song = Song(random_artist, artist_id=artist_id)
    current_game = GuessingGames(current_song)
    # current_game.easy()
    # current_game.medium()
    current_game.hard()


main()
