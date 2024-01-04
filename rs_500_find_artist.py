from pathlib import Path

# Import the cleaned up file and read the content, then split lines into items in a list.
path = Path('albums_cleaned.csv')
content = path.read_text()
albums = content.splitlines()

# Create the search term.
search_term = str('The Beatles')

# See if it's in the raw content first. 
# If it is, then find the index and info and print it out for each occurrence. 
# If not, then print a sorry message.
if search_term in content: 
    print(search_term + " was found in Rolling Stone's Top 500 Albums list!")

    for s in albums:
        position = str(albums.index(s))
        album_info_raw = albums.index(s)
        album_info = albums[album_info_raw].split(',')
        album = album_info[2]
        if search_term in str(s):
            print(search_term + " was ranked " + position + " for " + album + ".")
    
else:
    print("Sorry, " + search_term + " didn't make the cut.")