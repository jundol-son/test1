import requests
import json

url = "https://golmok.seoul.go.kr/region/selectIncome.json"

data = {
    'stdrYyCd': '2023',
    'stdrSlctQu': 'sameQu',
    'stdrQuCd': '3',
    'stdrMnCd': '202309',
    'selectTerm': 'quarter',
    'svcIndutyCdL': 'CS000000',
    'svcIndutyCdM': 'all',
    'stdrSigngu': '11',
    'selectInduty': '1',
    'infoCategory': 'income',
}

resp = requests.post(url, data=data)
result = resp.json()
print(result)
for item in result:
    print(item['NM'], item['INCOME_SCTN_CD_3'])
