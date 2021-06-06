import requests
from bs4 import BeautifulSoup
print("User Input | Crypto Prices (USD)")
print("---------------------------------------------------")
session = requests.Session()
repeat = 'y'
while repeat == 'y':
    coin = input("Enter A Crypto Ticker:\n")
    URL = 'https://finance.yahoo.com/quote/' + coin  + '-USD?p=' + coin +'-USD'
    page = session.get(URL)

    