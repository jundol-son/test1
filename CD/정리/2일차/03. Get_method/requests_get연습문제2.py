import requests
from bs4 import BeautifulSoup

url = "https://game.daum.net/"
# headers = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
# }

resp = requests.get(url)
# resp = requests.get(url, headers=headers)
css = "#mArticle > div.section_game > div:nth-child(3) > div > ul > li > a > span > strong"

if resp.status_code == 200:
    bs = BeautifulSoup(resp.text, 'html.parser')
    tags = bs.select(css)
    # print(tags[0].text)
    for i in tags:
        print(i.contents[0].text.strip())

