# import the library
from bs4 import BeautifulSoup

# GET request 
import requests

# use bs4 to scrape
# make a get request to the url
output = requests.get("https://github.com/pittcsc/Summer2022-Internships")
soup = BeautifulSoup(output.text, 'html.parser')

raw_table = soup.find_all('table')[0]