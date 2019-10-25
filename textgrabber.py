import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

mostActiveStocksUrl = "https://uk.reuters.com/article/uk-sudan-politics-southsudan/south-sudan-offers-to-mediate-political-transition-in-sudan-idUKKCN1RT23U";
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}
r = requests.get(mostActiveStocksUrl, headers=headers)
data = r.text
soup = BeautifulSoup(data)

table = soup.find_all('div', attrs={"class": "StandardArticleBody_body"})
print(table)
# all_rows=table.children
for x in table:
    print(x.find('p').text)
