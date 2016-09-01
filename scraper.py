import urllib2
from bs4 import BeautifulSoup

url = "http://www.indeed.com/jobs?q=security&l="
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

print soup.prettify()