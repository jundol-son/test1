import requests
import time

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

    url = 'https://golmok.seoul.go.kr/analysis/selectAnalysisAptHshldCo.json'
    data = {
        'name':'송정동',
        'wkt': item['wkt'],
        'area': item['relmAr'],
        'analysisRelm': item['relmAr'],
        'gbnCd': 'ADSTRD',
        'adstrdCd': item['adstrdCd'],
        'svcIndutyCd': 'CS000000',
        'svcIndutyNm': '업종전체',
        'stdrYyCd': '2023',
        'stdrQuCd': '3'
    }

    resp = requests.post(url, data=data)
    sub = resp.json()

    print(item['rn'], item['adstrdNm'], item['signguNm'], sub['TRDAR_TOT_HSHLD_CO_BF_4'])
    time.sleep(0.5)