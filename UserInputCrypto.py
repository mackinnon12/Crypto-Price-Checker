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
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    print(coin.upper() + "-USD: $" + results)
    repeat = input("Enter a different ticker? (y/n)\n")
    