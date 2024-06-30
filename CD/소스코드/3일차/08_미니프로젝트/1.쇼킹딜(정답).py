import requests
from bs4 import BeautifulSoup

url = "https://deal.11st.co.kr/browsing/DealAction.tmall?method=getShockingDealMain"
html = requests.get(url)

titles = []
prices = []
discounts = []

soup = BeautifulSoup(html.text, 'html5lib')
sel = '#layBody > section:nth-child(3) > div.c_list_card.c_list_card_collection.col_4 > ul > li > div > a > div.c-card-item__info > dl > div.c-card-item__name > dd'
result = soup.select(sel)
for tag in result:
    titles.append(tag.text.strip())

sel = '#layBody > section:nth-child(3) > div.c_list_card.c_list_card_collection.col_4 > ul > li > div > a > div.c-card-item__info > dl > div.c-card-item__price-info > dd.c-card-item__price > span.value'
result = soup.select(sel)
for tag in result:
    prices.append(tag.text.strip())

sel = '#layBody > section:nth-child(3) > div.c_list_card.c_list_card_collection.col_4 > ul > li > div > a > div.c-card-item__info > dl > div.c-card-item__price-info > dd.c-card-item__rate > span.value'
result = soup.select(sel)
for tag in result:
    discounts.append(tag.text.strip())

with open('2일차/11.csv', 'w') as f:
    for i in range(len(titles)):
        f.write(f'"{titles[i]}", "{prices[i]}", {discounts[i]}\n')