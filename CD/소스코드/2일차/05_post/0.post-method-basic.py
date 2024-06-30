import requests

url = "https://translate.kakao.com/translator/translate.json"
headers = {    
    'Referer': 'https://translate.kakao.com',    
}

data = {
    'queryLanguage': 'auto',
    'resultLanguage': 'kr',
    'q': 'hi, there'
}

resp = requests.post(url, data=data, headers=headers)
print(resp.text)
