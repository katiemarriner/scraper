import requests
from bs4 import BeautifulSoup

print "What is the URL you are scraping?"
url = raw_input()
r = requests.get(url)

soup = BeautifulSoup(r.content)

print "What is the name of the tag you want to search?"
tag = raw_input()
all_data = soup.find_all(tag)

f = open('index.html', 'w')

print >> f, "<html><head></head><body>"

for item in all_data:
    print >> f, (item.contents[1].text).encode('utf-8')
  	### READ THIS ABOUT UNICODE: https://docs.python.org/2/howto/unicode.html

print >> f, "</body></html>"

f.close()

