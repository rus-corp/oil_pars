import requests
from bs4 import BeautifulSoup
import urllib3
import os
from fake_useragent import FakeUserAgent
import fake_useragent
from pprint import pprint
import lxml
import re
import time
import json



catalog_dict = {}
def get_page():
    for i in range(1, 700):
        url = f'https://www.exist.ru/Catalog/Goods/7/3?Page={i}'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        result = soup.find_all(attrs={'class':'cell2'})
        for res in result:
            name = res.find(attrs={'class':'wrap'}).find('p').text
            price = res.find(attrs={'class':'ucatprcdiv'}).find('span').text
            price1 = re.sub('[\xa0]', '', price)
            catalog_dict[name] = price1

        


# def main():
#     for i in range(1, 975):
#         url = 'https://www.exist.ru/Catalog/Goods/7/3?Page={i}'
#         get_page()

if __name__ == '__main__':
    get_page()
    with open ('data.json', 'w', encoding='utf-8') as file:
        json.dump(catalog_dict, file, indent=4, ensure_ascii=False)




