from bs4 import BeautifulSoup
from pathlib import Path
import requests
import sys

# Create a list of URLs to search through. 
urls = [
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/',
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/linda-mccartney-and-paul-ram-1062783/',
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/the-go-gos-beauty-and-the-beat-1062833/',
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/stevie-wonder-music-of-my-mind-2-1062883/',
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/shania-twain-come-on-over-1062933/',
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/buzzcocks-singles-going-steady-2-1062983/',
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/sade-diamond-life-1063033/',
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/bruce-springsteen-nebraska-3-1063083/',
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/the-band-music-from-big-pink-2-1063133/',
    'https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/jay-z-the-blueprint-3-1063183/'
]

# Create an empty list to hold the album results. 
rs_500 = []

# Search the URLs and return all H2 content to get the albums and artists.
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    albums = soup.find_all("h2")

    # Clean up the results a bit, then dump them in the rs_500 list.
    for raw_album in albums:
        album = raw_album.text.strip().replace(', ', ',').replace('‘', '').replace('’', '')
        rs_500.append(album)    

# Each page has some H2 elements that are not albums. Remove them. 
remove_from_rs_500 = ["The Latest", "Most Popular", "You might also like"]
rs_500 = [album for album in rs_500 if album not in remove_from_rs_500]

# Reverse the order they're pulled to get the rank of each album to match the index of the list. 
rs_500.reverse()

# Create an albums.csv file and write the indexes and items of rs_500 to the file. 
with open('albums.csv', 'w') as f:
    for (i, item) in enumerate(rs_500, start=1):
        f.write(str(i))
        f.write(',')
        f.write(item)
        f.write(',')
        f.write('\n')