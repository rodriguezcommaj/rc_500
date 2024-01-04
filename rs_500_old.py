from bs4 import BeautifulSoup
from pathlib import Path
import requests
import sys

url_1 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/"
page = requests.get(url_1)

soup = BeautifulSoup(page.content, 'html.parser')

rs_500 = []

albums_1 = soup.find_all("h2")

for raw_album in albums_1:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

url_2 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/linda-mccartney-and-paul-ram-1062783/"
page = requests.get(url_2)

soup = BeautifulSoup(page.content, 'html.parser')

albums_2 = soup.find_all("h2")

for raw_album in albums_2:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

url_3 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/the-go-gos-beauty-and-the-beat-1062833/"
page = requests.get(url_3)

soup = BeautifulSoup(page.content, 'html.parser')

albums_3 = soup.find_all("h2")

for raw_album in albums_3:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

url_4 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/stevie-wonder-music-of-my-mind-2-1062883/"
page = requests.get(url_4)

soup = BeautifulSoup(page.content, 'html.parser')

albums_4 = soup.find_all("h2")

for raw_album in albums_4:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

url_5 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/shania-twain-come-on-over-1062933/"
page = requests.get(url_5)

soup = BeautifulSoup(page.content, 'html.parser')

albums_5 = soup.find_all("h2")

for raw_album in albums_5:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

url_6 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/buzzcocks-singles-going-steady-2-1062983/"
page = requests.get(url_6)

soup = BeautifulSoup(page.content, 'html.parser')

albums_6 = soup.find_all("h2")

for raw_album in albums_6:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

url_7 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/sade-diamond-life-1063033/"
page = requests.get(url_7)

soup = BeautifulSoup(page.content, 'html.parser')

albums_7 = soup.find_all("h2")

for raw_album in albums_7:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

url_8 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/bruce-springsteen-nebraska-3-1063083/"
page = requests.get(url_8)

soup = BeautifulSoup(page.content, 'html.parser')

albums_8 = soup.find_all("h2")

for raw_album in albums_8:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

url_9 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/the-band-music-from-big-pink-2-1063133/"
page = requests.get(url_9)

soup = BeautifulSoup(page.content, 'html.parser')

albums_9 = soup.find_all("h2")

for raw_album in albums_9:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

url_10 = "https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/jay-z-the-blueprint-3-1063183/"
page = requests.get(url_10)

soup = BeautifulSoup(page.content, 'html.parser')

albums_10 = soup.find_all("h2")

for raw_album in albums_10:
    album = raw_album.text.strip().replace('‘', '').replace('’', '')
    rs_500.append(album)

remove_from_rs_500 = ["The Latest", "Most Popular", "You might also like"]
rs_500 = [album for album in rs_500 if album not in remove_from_rs_500]

with open('albums.csv', 'w') as f:
    for line in rs_500:
        f.write(line)
        f.write(',')
        f.write('\n')

# print(len(rs_500))

# for entry in rs_500:
#     print(entry)