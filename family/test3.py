from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import time

# ChromeDriver 경로를 지정하지 않으면, 아래 코드가 최신 드라이버를 자동으로 설치해줍니다.
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 크롤링할 URL
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EA%B5%AD%EA%B5%AD%EC%B1%84'

# 페이지 로드
driver.get(url)

# 페이지가 완전히 로드될 때까지 잠시 대기 (필요에 따라 조정)
time.sleep(2)


print("금리 찾기")
search_list = ['한국 국채', '미국 국채']
find_list = []
price_list = []

def price_find(item): 
    search_box = driver.find_element(By.CSS_SELECTOR, "#nx_query")
    search_box.clear()  # 검색창 초기화
    search_box.send_keys(item)
    search_button = driver.find_element(By.CSS_SELECTOR, "#nx_search_form > fieldset > button > i")
    search_button.click()
    try:
        if "국채" in item:
            for i in range(5):
                xpath = f'//*[@id="main_pack"]/div[3]/div[2]/div/div/div/div[2]/div[1]/ul[1]/li[{i+1}]/a/div[1]/strong'
                find_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                find_list.append(find_name.text)
                xpath = f'//*[@id="main_pack"]/div[3]/div[2]/div/div/div/div[2]/div[1]/ul[1]/li[{i+1}]/a/div[2]/span[1]'
                find_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                price_list.append(find_name.text)
        elif "환율" in item:
            xpath = '//*[@id="main_pack"]/section[1]/div[1]/div[3]/div[1]/a/div[2]/strong'
        else:
            print(f"아이템 '{item}'에 대한 적절한 XPath를 찾을 수 없습니다.")
            return
    except NoSuchElementException:
        print(f"아이템 '{item}'에 대한 가격 요소를 찾을 수 없습니다.")
    except TimeoutException:
        print(f"아이템 '{item}'에 대한 가격 요소를 찾는 데 시간이 초과되었습니다.")

for i in search_list:
    price_find(i)

data = {'종목': find_list, '금리(국채) , 가격(환율)': price_list}
df = pd.DataFrame(data)
# df_sorted = df.sort_values(by='종목', ascending=True)

# DataFrame 출력
print(df)
# print(df_sorted)
# 요소 선택
# try:
#     element = driver.find_element(By.CSS_SELECTOR, "#main_pack > div.sc_new.cs_common_module.case_list.color_5._finance_bond_yield > div.cm_content_wrap > div > div > div > div.percent_box_list > div._panel_wrapper > ul:nth-child(1) > li:nth-child(1) > a > div.title_box > strong")
#     print(element.text)  # 요소의 텍스트 출력
# except Exception as e:
#     print("해당 요소를 찾을 수 없습니다.", e)

# 브라우저 종료