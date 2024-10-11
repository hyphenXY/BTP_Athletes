# on a webpage, click right click and select "view page source" to see the html code

import requests
from bs4 import BeautifulSoup

with open('worldathletics.html', 'w') as f:
    f.write('')

page=1

while page<=35:
    url = f'https://worldathletics.org/world-rankings/marathon/men?regionType=world&page={page}&rankDate=2024-10-08&limitByCountry=0'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # paste it in a file

    with open('worldathletics.html', 'a') as f:
        f.write(soup.prettify())
        
    page+=1
    
#  click on next page

