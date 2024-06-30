import requests
import json

url = "https://smartstore.naver.com/i/v1/contents/reviews/query-pages"
headers = {     
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',       
}

data = {
    "checkoutMerchantNo": 510561930,
    "originProductNo": 4776042673,
    "page": 1,
    "pageSize": 20,
    "reviewSearchSortType": "REVIEW_RANKING"
}

resp = requests.post(url, data=data, headers=headers)
data = resp.json()
for item in data['contents']:
    print(item['reviewContent'])
