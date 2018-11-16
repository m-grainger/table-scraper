import urllib.request
from bs4 import BeautifulSoup as bs

def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = bs(thepage, "html.parser")
	return soupdata

soup = make_soup("<insert URL here>")	

row_recent = []
for row in soup.findAll('tr', class_="name-sublevel1-even", limit=1):
	row_recent.append(row.text)
for x in row_recent:print(x)
