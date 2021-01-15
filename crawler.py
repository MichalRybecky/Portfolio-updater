"""
Yahoo Finance current stock price crawler
- takes ticker symbols from ticker-symbols.txt
- returns list of dictionaries with ticker symbol and it's current price
"""

import requests
from bs4 import BeautifulSoup


def get_urls(tickers_dict: dict) -> list:
    """
    returns list of dictionaries with ticker symbol and it's Yahoo Finance url
    """
    tickers = [next(iter(ticker.values())) for ticker in tickers_dict]
    urls = []
    for ticker in tickers:
        urls.append(
            {
                "ticker": ticker,
                "url": f"https://finance.yahoo.com/quote/{ticker}?p={ticker}",
            }
        )
    return urls


def get_prices(tickers) -> dict:
    """
    returns dict of dictionaries with ticker symbol and it's current price
    """
    prices = {}
    urls = get_urls(tickers)
    for url in urls:
        response = requests.get(url["url"])
        PAGE_HTML = response.text
        soup = BeautifulSoup(PAGE_HTML, "html.parser")
        try:
            price = soup.find("span", attrs={"data-reactid": "32"}).text
        except AttributeError:
            price = "Unable to parse, check ticker!"
        ticker_name = url['ticker']
        prices.update({ticker_name: price})
    return prices
