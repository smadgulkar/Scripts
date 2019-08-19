import requests
from bs4 import BeautifulSoup

url = 'https://www.livemint.com/topic/'

links = []

r = requests.get(url)

print(r.text)

# soup = BeautifulSoup(r.text,'html5lib')

# for a in soup.find_all('p', href=True):
#     print(a)