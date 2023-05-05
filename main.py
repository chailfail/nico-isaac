import requests
from random import randint
from spotify_user import SpotifyUser
from spotify_library import authorize_and_get_token
from genius_lyrics_library import Song, GuessingGames

# dict of genius artist ids with obscure or generic names to make them easier for the geniuslyrics library to find
artist_ids = {
    "Jons": 1055422,
}


# FIXME: when guessing words, punctuation is sometimes included
# FIXME: the wrong apostrophe in a lyric can make a correct guess incorrect (’ instead of ')
# FIXME: The Beatles sometimes raises a TimeoutError, not sure why

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
    current_song = None
    game_mode = None
    while game_mode != "artist" and game_mode != "track":
        game_mode = input("\nChoose gamemode (artist or track): ").lower()
        if game_mode == "artist":
            random_artist = user_top_artists[randint(0, 9)]
            artist_id = artist_ids.get(random_artist)
            print()
            current_song = Song(random_artist, artist_id=artist_id)
        elif game_mode == "track":
            while current_song is None:
                random_track = user_top_tracks[randint(0, 9)]
                current_song = Song(artist=random_track["artist"], title=random_track["title"])
                if current_song.song is None:
                    current_song = None
        else:
            print("Please enter a valid gamemode.")
    current_game = GuessingGames(current_song)
    difficulty = None
    while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        difficulty = input("\nEnter difficulty (easy, medium, or hard): ")
        if difficulty.lower() == "easy":
            current_game.easy()
        elif difficulty.lower() == "medium":
            current_game.medium()
        elif difficulty.lower() == "hard":
            current_game.hard()
        else:
            print("Please enter a valid difficulty.")


main()
