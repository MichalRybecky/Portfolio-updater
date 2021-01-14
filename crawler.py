"""
Yahoo Finance current stock price crawler
- takes ticker symbols from ticker-symbols.txt
- returns list of dictionaries with ticker symbol and it's current price
"""

import requests
from bs4 import BeautifulSoup


def get_urls() -> list:
    """
    returns list of dictionaries with ticker symbol and it's Yahoo Finance url
    """
    with open('ticker-symbols.txt', 'r') as file:
        tickers = [line.strip() for line in file]
    urls = []
    for ticker in tickers:
        urls.append({'ticker': ticker, 'url': f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'})
    return urls


def get_prices() -> list:
    """
    returns list of dictionaries with ticker symbol and it's current price
    """
    prices = []
    for url in get_urls():
        response = requests.get(url['url'])
        PAGE_HTML = response.text
        soup = BeautifulSoup(PAGE_HTML, 'html.parser')
        price = soup.find('span', attrs={"data-reactid": "32"}).text
        prices.append({'ticker': url['ticker'], 'price': float(price)})
    return prices

