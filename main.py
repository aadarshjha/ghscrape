# import the library
from bs4 import BeautifulSoup

# GET request 
import requests

# use bs4 to scrape
# make a get request to the url
output = requests.get("https://github.com/pittcsc/Summer2022-Internships")
soup = BeautifulSoup(output.text, 'html.parser')
# print(soup.prettify())
print(len(soup.find_all('table')))

print(soup.find_all('table')[0])

# save the soup.find_all('table')[0] to a file
with open('output.html', 'w') as f:
    f.write(soup.find_all('table')[0])
