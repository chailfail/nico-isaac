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

def guess_song_easy(song):
    """Takes a song and prints the lyrics one line at a time, allowing the user to guess the title of the song every loop"""
    lyrics = song.lyrics
    lines = lyrics.split("\n")
    line = 1
    guess = ""
    while guess != song.title and line < 6:
        print(lines[line])
        guess = input("What is the title?\n")
        line += 1
    if line > 5:
        print("The song title was {}. Better luck next time!".format(song.title))
    else:
        print("Great job! {} is correct!".format(song.title))

def guess_song_medium(song):
    """Takes a song and chooses a line to remove a lyric from. Prints all lines up until line with removed character. Prints line with removed character and asks user to guess 5 times."""
    lyrics = song.lyrics
    lines = lyrics.split("\n")  # creates a list of all lyrics
    line_num_to_affect = randint(1, len(lines)) # finds the index of a line which will be accessed
    for i in range(1, line_num_to_affect):
        print(lines[i])  # prints the lyrics up until the line accessed
    line_to_affect = lines[line_num_to_affect].split()  # creates a list of all words in the accessed line
    word_to_remove_num = randint(0, len(line_to_affect))  # creates an index of the word to remove from the line
    removed_word = line_to_affect[word_to_remove_num]  # stores the word to be removed
    line_to_affect[word_to_remove_num] = "_" * len(removed_word)
    for i in range(len(line_to_affect)):
        print(line_to_affect[i], end=" ")
    guess_num = 1
    guess = ""
    while guess_num <= 5 and guess != removed_word:
        guess = input("What is the missing word?")
        guess_num += 1
    if guess == removed_word:
        print("Great guess! You were right, the missing word was {}.".format(removed_word))
    else:
        print("Better luck next time! The missing word was {}.".format(removed_word))

def main():
    genius = lyricsgenius.Genius("-MiAj7fIqCsxQ0Unn95GJVh6DlRwnyiQjG16nDTk_MDoowDwekuJX5pwVZLRcmng")
    # ^creates an object which stores the Genius API request
    genius.remove_section_headers = True
    # ^removes things like [chorus] or [verse 1]
    song = choose_song(genius, "Faye Webster")
    #guess_song_easy(song)
    guess_song_medium(song)

main()