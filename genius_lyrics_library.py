import lyricsgenius
from random import randint


class Song:

    def __init__(self, artist, title=None, artist_id=None):
        self.artist = artist
        self.genius = lyricsgenius.Genius("-MiAj7fIqCsxQ0Unn95GJVh6DlRwnyiQjG16nDTk_MDoowDwekuJX5pwVZLRcmng")  # API key
        self.genius.remove_section_headers = True  # removes [chorus] and [verse]
        if title:
            self.gamemode = "track"
            self.song = self.genius.search_song(title, artist)
        else:
            self.gamemode = "artist"
            self.artist_obj = self.genius.search_artist(artist, max_songs=5, sort="popularity", artist_id=artist_id)
            # ^you can sort by: "title", "popularity"
            # ^^by removing max_songs it will store all songs from artist
            self.song = None
            self.choose_song()
        if self.song is not None:
            self.lyrics = self.song.lyrics
            self.title = self.song.title
        album_search_results = self.genius.search_albums(artist)
        self.albums = [hit["result"] for hit in album_search_results["sections"][0]["hits"]]

    def choose_song(self):
        """ :returns: one song from an artist's five most popular."""
        songs = self.artist_obj.songs  # gets the artist's 5 most popular songs
        song_num = randint(0, 4)
        self.song = songs[song_num]

    def change_artist(self, new_artist):
        """ :param: A new artist to look for. changes necessary information."""
        self.artist = new_artist
        self.artist_obj = self.genius.search_artist(new_artist, max_songs=5, sort="popularity", artist_id=None)
        self.choose_song()
        self.lyrics = self.song.lyrics
        self.title = self.song.title


class GuessingGames:

    def __init__(self, song):
        self.song = song
        self.lyrics = self.song.lyrics
        self.lines = self.lyrics.split("\n")
        self.clean_lines()
        self.title = song.title
        self.artist = song.artist
        self.albums = self.song.albums

    def clean_lines(self):
        blank_line_list = []
        for i in range(len(self.lines)):
            if self.lines[i] == "":
                blank_line_list.append(i)
        difference = 0
        for i in range(len(blank_line_list)):
            del self.lines[blank_line_list[i]-difference]
            difference += 1
        letter_list = []
        for i in range(len(self.lines[-1])):
            letter_list.append(self.lines[-1][i])
        final_word = ""
        for letter in letter_list:
            if 65 <= ord(letter) <= 122 or 32 <= ord(letter) <= 46:
                final_word += letter
            else:
                break
        self.lines[-1] = final_word

    def easy(self):
        """Easy version of guessing game"""
        wins = 0
        losses = 0
        line_num_to_affect = randint(1, len(self.lines) - 1)  # finds the index of a line which will be accessed
        for j in range(line_num_to_affect):
            print(self.lines[j])  # prints the lyrics up until the line accessed
        line_to_affect = self.lines[line_num_to_affect].split(" ")  # use the line with index line_num_to_affect and split it into words
        while len(line_to_affect) < 2:  # Check if the line has at least two words
            line_num_to_affect = randint(1, len(self.lines) - 1)
            line_to_affect = self.lines[line_num_to_affect].split(" ")
        word_to_remove_num = randint(0, len(line_to_affect) - 1)  # picks random word number to remove
        removed_word = line_to_affect[word_to_remove_num]  # stores the word to be removed
        line_to_affect[word_to_remove_num] = "_" * len(removed_word)
        for word in line_to_affect:
            print(word, end=" ")
        guess_num = 1
        guess = ""
        while guess_num <= 5 and guess != removed_word:
            guess = input("\nWhat is the missing word?\n")
            guess_num += 1
        if guess == removed_word:
            print("Great guess! You were right, the missing word was '{}'.".format(removed_word))
            wins += 1
        else:
            print("Better luck next time! The missing word was '{}'.".format(removed_word))
            losses += 1
        print()
    print("Great game! You had {} wins and {} losses.".format(wins, losses))

    def medium(self):
        """Medium version of guessing game"""
        wins = 0
        losses = 0
        for i in range(3):
            print(f"\nSong: {self.title}")
            print(f"\nAlbums by {self.artist}:")
            for index, album in enumerate(self.albums):
                print(f"{index + 1}. {album['name']}")
            attempts = 3
            correct_album = None
            genius = lyricsgenius.Genius("-MiAj7fIqCsxQ0Unn95GJVh6DlRwnyiQjG16nDTk_MDoowDwekuJX5pwVZLRcmng")
            for album in self.albums:
                tracklist = []
                album_tracks_search = genius.album_tracks(album['id'])
                for result in range(len(album_tracks_search['tracks'])):
                    track = album_tracks_search['tracks'][result]['song']['title']
                    tracklist.append(track)
                    if self.title in tracklist:
                        correct_album = album['name']
                        break
            while attempts > 0:
                guess = int(input("\nGuess the album number (1-{}): ".format(len(self.albums)))) - 1
                if self.albums[guess]['name'] == correct_album:
                    print("Great job! That's the correct album!")
                    wins += 1
                    break
                else:
                    print("Sorry, that's not the correct album. Try again.")
                    attempts -= 1
            if attempts == 0:
                print(f"The correct album was {correct_album}. Better luck next time!")
                losses += 1
            print()
        print("Great game! You had {} wins and {} losses.".format(wins, losses))

    def hard(self):
        """Hard version of guessing game"""  # make all games loop a few times, ask a few different questions
        wins = 0
        losses = 0
        for i in range(3):
            line_num_to_affect = randint(1, len(self.lines))  # finds the index of a line which will be accessed
            line_to_affect = self.lines[line_num_to_affect].split()  # creates a list of all words in the accessed line
            word_to_remove_num = randint(0, len(line_to_affect)-1)  # creates an index of the word to remove from the line
            removed_word = line_to_affect[word_to_remove_num]  # stores the word to be removed
            line_to_affect[word_to_remove_num] = "_" * len(removed_word)
            for i in range(len(line_to_affect)):
                print(line_to_affect[i], end=" ")
            guess_num = 1
            guess = ""
            while guess_num <= 5 and guess != removed_word:
                guess = input("\nWhat is the missing word?\n")
                guess_num += 1
            if guess == removed_word:
                print("Great guess! You were right, the missing word was '{}'.".format(removed_word))
                wins += 1
            else:
                print("Better luck next time! The missing word was '{}'.".format(removed_word))
                losses += 1
            print()
        print("Great game! You had {} wins and {} losses.".format(wins, losses))


def main():
    print("start")
    new_song = Song("steve lacy")
    print(new_song.lyrics)
    games = GuessingGames(new_song.song)
    print(games.lines)
    print(new_song)
    # games.easy()
    # new_song.choose_song()
    # games.medium()
    # new_song.choose_song()
    # games.hard()


if __name__ == "__main__":
    main()
