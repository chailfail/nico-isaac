from flask import Flask
import requests
from random import randint
from spotify_user import SpotifyUser
from spotify_library import authorize_and_get_token
from genius_lyrics_library import Song, GuessingGames

app = Flask(__name__)


artist_ids = {
    "Jons": 1055422,
}


@app.route('/')
def home():
    return """
        <html><body>
         <h2>Welcome to the Lyrics Guessing Game!</h2>
         <h2>Choose your gamemode:</h2>
         <a href="/easy">Easy</a>
         <br>
         <a href="/medium">Medium</a>  
         <br>
         <a href="/hard">Hard</a>
     </body></html>
 """


@app.route('/easy')
def easy():
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
    return """
    <html><body>
    {}
    </body></html>
    """.format(current_game.easy())


@app.route('/medium')
def medium():
    pass


@app.route('/hard')
def hard():
    pass


if __name__ == "__main__":
    app.run(host="localhost", port=9000, debug=True)
