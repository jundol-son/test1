import requests

def translate(korean):
    url = "https://translate.kakao.com/translator/translate.json"
    headers = {    
        'Referer': 'https://translate.kakao.com',    
    }

    data = {
        'queryLanguage': 'kr',
        'resultLanguage': 'en',
        'q': korean
    }

    resp = requests.post(url, data=data, headers=headers)
    data = resp.json()

    return data['result']['output'][0][0]

dat = translate('안녕하세요. 반갑습니다.')
print(dat)