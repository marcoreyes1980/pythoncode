
import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search?q=Unix%2FLinux+Administrator&where=texas'

page = requests.get(URL)

soup = BeautifulSoup(page.text, 'lxml')

results = soup.find(id='app')

#print(results.prettify())
job_elems = results.find_all('div', id = 'results-card')
for job_elem in job_elems:
    title_elem = job_elem.find('div', class_= 'title-company-location')
    print(title_elem)
