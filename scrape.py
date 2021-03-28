import requests
from bs4 import BeautifulSoup
URL = 'http://pythonjobs.github.io/'

page = requests.get(URL)

soup= BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='container')
#
job_elems = soup.find_all('div', class_='job')

for job_elem in job_elems:
    title_elem = job_elem.find('h1')
    location_elem = job_elem.find('span', class_='info')
    deets_elem = job_elem.find('p', class_='detail')
    print(title_elem.text)
    print(location_elem.text)
    print(deets_elem.text)
    print()



