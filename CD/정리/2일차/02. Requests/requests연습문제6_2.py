from bs4 import BeautifulSoup
import requests
def get_per(code):
    url = f"https://finance.naver.com/item/main.nhn?code={code}"
    resp = requests.get(url)
    css = "#_per"
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        tags = soup.select_one(css)
        if tags:
            return(tags.text)
        # else:
        #     return(tags)
    
print(get_per("005930"))
print(get_per("000660"))