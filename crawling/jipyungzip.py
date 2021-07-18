#beautifulsoup4, selenium,  install requests 가 깔려있어야 함
from selenium import webdriver as wb #webdriver는 웹을 통제하기 위한 모듈
from selenium.webdriver.common.keys import Keys #Keys는 웹을 제어하면서 값을 입력하기 위한 모듈
import time
import requests as req
from bs4 import BeautifulSoup as bs

#ㄹ방
driver =wb.Chrome() #실행시키면 크롬 빈창이 나옴, chromedriver이 실행파일과 동일한 위치 상에 있는지, 아니라면 경로조정
url = "http://jipyungzip.com/reservation?idx=11&day=2021-11-13" #url 변수에 가져오고 싶은 페이지 주소 문자형태로 넣은 것 뿐 
driver.get(url)  #driver변수에 url집어 넣어줌

while True:
    try:
        button1 = driver.find_element_by_css_selector('a.buy')
        button1.click()
        time.sleep(0.1)
        alert = driver.switch_to.alert #띄워진 자바스크립트 alert창 없애기
        alert.accept()
    except:
        time.sleep(0.1)
        orderName = driver.find_element_by_css_selector('input._orderer_name')
        orderName.send_keys("김동일")
        orderCall = driver.find_element_by_css_selector('input._orderer_call')
        orderCall.send_keys("010-4903-7595")
        orderEmail = driver.find_element_by_css_selector('input._orderer_email')
        orderEmail.send_keys("kdi1569@gmail.com")
        agreeButton = driver.find_element_by_css_selector('span.text-13') #동의합니다 버튼
        agreeButton.click()
        allAgreeButton = driver.find_element_by_css_selector('span.text-14') #전체 동의합니다 버튼
        allAgreeButton.click()
        paymentButton = driver.find_element_by_css_selector('a._btn_start_payment') #결제 버튼
        paymentButton.click()