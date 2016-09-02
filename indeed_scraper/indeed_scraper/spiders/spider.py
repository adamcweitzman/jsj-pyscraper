import urllib2
from bs4 import BeautifulSoup

url = "http://www.indeed.com/jobs?q=security&l="
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

all_tables=soup.find_all("div", class_="result")

print all_tables