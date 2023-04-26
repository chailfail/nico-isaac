import lyricsgenius

genius = lyricsgenius.Genius("-MiAj7fIqCsxQ0Unn95GJVh6DlRwnyiQjG16nDTk_MDoowDwekuJX5pwVZLRcmng") # creates an object which stores the Genius API request
genius.remove_section_headers = True # removes things like [chorus] or [verse 1]
artist = genius.search_artist("The Strokes", max_songs=5, sort="popularity")
# by removing max_songs it will store all songs from artist
# you can sort by: "title", "popularity"
print(artist.songs)

song = artist.song("Selfless")
print(song.lyrics)