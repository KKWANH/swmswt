from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 현재 폴더 위치 넣기
folder = '/Users/kimkwanho/Documents/swmsweetsmacro'

# Chrome 옵션 생성 및 웹 드라이버 초기화
path = f'{folder}/chromedriver_mac64/chromedriver'  # 크롬 드라이버 경로를 지정해야 합니다.

# 카운트 변수
success = 0
failure = 0
# 반복문 회수 변수
count = 3

# 반복문
for i in range(count):
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
    sleep(1)
    # 이동된 URL 확인
    current_url = driver.current_url
    
    # 완료 카운트
    if current_url[-6:] == "share/":
        print("성공 :", current_url[-6:])
        success += 1
    else:
        print("실패 :", current_url[-6:])
        failure += 1
    # 웹 드라이버 종료
    driver.quit()
    sleep(0.5)

print("성공 횟수: ", success)
print("실패 횟수: ", failure)

