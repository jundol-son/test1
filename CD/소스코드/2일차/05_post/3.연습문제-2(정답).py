import requests
import json

url = "https://golmok.seoul.go.kr/common/code/getNewTrdarList.json"

data = {
    'searchTab': 'searchCommercialTown',
    'searchSubTab': 'searchTabStoreCnt',
    'searchParmStandard': 'addRate',
    'indutyLclasCd': 'CS000000',
    'indutyCd': '',
    'searchParmAge': 'searchAgeAll',
    'searchParmSex': 'G',
    'searchParmQt': '1',
    'searchParmDay': 'A',
    'selectSignguCd': '',
    'allAreaTf': 'false',
    'xCntsMin':'', 
    'xCntsMax':'', 
    'yCntsMin':'', 
    'yCntsMax':'', 
    'stdrSlctQu': 'beforeQu',
    'searchYear': '', 
    'searchPeriod': 'qu',
}

resp = requests.post(url, data=data)
result = resp.json()
print(result)
for item in result:
    print(item['rn'], item['adstrdNm'], item['signguNm'])
