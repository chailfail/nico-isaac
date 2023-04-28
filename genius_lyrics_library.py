import lyricsgenius
from random import randint


def choose_song(genius, artist_name):
    """chooses a song from an artists 5 most popular songs"""
    artist_obj = genius.search_artist(artist_name, max_songs=5, sort="popularity")
    # ^you can sort by: "title", "popularity"
    # ^^by removing max_songs it will store all songs from artist
    songs = artist_obj.songs
    song_num = randint(0, 4)
    return songs[song_num]

def guess_song(song):
    """Takes a song and prints the lyrics one line at a time, allowing the user to guess the title of the song every loop"""
    lyrics = song.lyrics
    print(lyrics)




def main():
    genius = lyricsgenius.Genius("-MiAj7fIqCsxQ0Unn95GJVh6DlRwnyiQjG16nDTk_MDoowDwekuJX5pwVZLRcmng")
    # ^creates an object which stores the Genius API request
    genius.remove_section_headers = True
    # ^removes things like [chorus] or [verse 1]
    song = choose_song(genius, "Faye Webster")
    guess_song(song)

main()