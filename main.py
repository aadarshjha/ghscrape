# import the library
import json
from bs4 import BeautifulSoup
import bs4

# GET request
import requests

# use bs4 to scrape
# make a get request to the url
output = requests.get("https://github.com/pittcsc/Summer2022-Internships")
soup = BeautifulSoup(output.text, 'html.parser')

raw_table = soup.find_all('table')[0]

# look for all th tags, and get the text
raw_headers = raw_table.find_all('th')

table_dict = {}

# make raw_headers into keys of table_dict
column_names = []
for header in raw_headers:
    table_dict[header.text] = []
    column_names.append(header.text)

# find all the table tr
raw_rows = raw_table.tbody.contents

for row in raw_rows:
    if type(row) != bs4.element.Tag:
        continue

    i = 0
    for td in row.children:
        if type(td) != bs4.element.Tag:
            continue
        # put it into the dictionary
        table_dict[column_names[i]].append(td.text)
        i += 1
