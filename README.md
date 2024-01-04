# rs_500

**Python project to scrape Rolling Stone's 500 Greatest Albums list into a single, easily digestible list.**

Mostly a learning project for myself. I wanted a way to easily search [Rolling Stone's 500 Greatest Albums](https://www.rollingstone.com/music/music-lists/best-albums-of-all-time-1062063/) and decided to use it as an opportunity to apply a little Python. In particular, I was looking to explore:

- Web scraping with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- Manipulating lists
- Writing data to files
- And reading and searching data from files

My first attempt is in `rs_500_old.py`, which is just a ton of the same calls to do the same thing. I cleaned all that up into a for loop in `rs_500.py`. The output `albums.csv` file is fairly dirty since I didn't do too much formatting to the scraped info. So I manually cleaned that up in Numbers and exported a few different file formats. 

`rs_500_find_artist.py` reads the cleaned up CSV file, then allows you to search for a term like an artist name. It looks through the data, finds all the indexes where that exists, and spits out the info in a nice, readable way. 


