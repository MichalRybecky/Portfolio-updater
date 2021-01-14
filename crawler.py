import requests
from bs4 import BeautifulSoup

page = "https://finance.yahoo.com/quote/CCIV?p=CCIV"
response = requests.get(page)
PAGE_HTML = response.text
soup = BeautifulSoup(PAGE_HTML, 'html.parser')
price = soup.find('span', attrs={"data-reactid": "32"}).text
print(price)
