from bs4 import BeautifulSoup
import requests

url = 'https://deal.11st.co.kr/browsing/DealAction.tmall?method=getShockingDealMain'
resp = requests.get(url)
css_price = "#layBody > section:nth-child(3) > div.c_list_card.c_list_card_collection.col_4 > ul > li > div > a > div.c-card-item__info > dl > div.c-card-item__price-info > dd.c-card-item__price > span.value"
css_name =  "#layBody > section:nth-child(3) > div.c_list_card.c_list_card_collection.col_4 > ul > li > div > a > div.c-card-item__info > dl > div.c-card-item__name > dd"
if resp.status_code == 200:
    if "우산 블랙" in resp.text:
        soup = BeautifulSoup(resp.text,'html.parser')
        result_price = soup.select(css_price)
        result_name = soup.select(css_name)

        l = len(result_price)
        i = 0
        with open("amazon.csv","w") as f:
            f.write("제품명,가격\n")
            while i < l:
                f.write(result_name[i].text.strip()+',"'+result_price[i].text.strip()+'",\n')
                i+=1
        # with open('amazon.csv', 'w') as f:
        # list_price = []
        # list_name = []
        # for i in result_price:
        #     list_price.append(i.text.strip())
        # for i in result_name:
        #     list_name.append(i.text.strip())

        # print(result_name)
        # with open('amazon.csv', 'w') as f:
        #     f.writelines(result_name)
        # for i in result_price:
        #     with open('amazon.csv', 'a') as f:
        #         f.write(i.text.strip)


    