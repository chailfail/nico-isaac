import lyricsgenius

genius = lyricsgenius.Genius("-MiAj7fIqCsxQ0Unn95GJVh6DlRwnyiQjG16nDTk_MDoowDwekuJX5pwVZLRcmng")

# Search for the artist
search_results = genius.search_artists("Jons-band")
print(search_results)

# Loop through the search results and find the correct artist
jons_artist_id = None
for section in search_results['sections']:
    for hit in section['hits']:
        if "jons" in hit['result']['name'].lower():
            jons_artist_id = hit['result']['id']
            break

print("Jons artist ID:", jons_artist_id)
