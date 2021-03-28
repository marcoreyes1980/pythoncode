import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/q-Linux-Administrator-jobs.html'

page = requests.get(URL)

soup= BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

results = soup.find(id='resultsBody')

#print(results.prettify())
job_elems =  results.find_all('div',   class_= 'jobsearch-SerpJobCard unifiedRow row result clickcard')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_ = 'title')
    print(title_elem)
