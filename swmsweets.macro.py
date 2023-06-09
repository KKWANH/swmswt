from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 현재 폴더 위치 넣기
folder = '/Users/kimkwanho/Documents/swmsweetsmacro'

# Chrome 옵션 생성 및 웹 드라이버 초기화
path = f'{folder}/chromedriver_mac64/chromedriver'  # 크롬 드라이버 경로를 지정해야 합니다.
service = Service(executable_path=path)
options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--single-process")
driver = webdriver.Chrome(service=service, options=options)

# 웹 사이트 열기
driver.get('https://www.10best.com/awards/travel/best-chocolate-shop-2023/stick-with-me-sweets-new-york-city-new-york/')  # 해당 사이트의 URL을 입력합니다.

# <a> 태그 요소 찾기
a_element = driver.find_element('id', 'awardVoteButton')  # 링크 주소를 실제로 바꿔주세요.
# 링크 클릭
a_element.click()

# 이동된 URL 확인
current_url = driver.current_url
print("현재 URL:", current_url)

# 웹 드라이버 종료
driver.quit()