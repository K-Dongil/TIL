import requests # requests 패키지 가져온다
from bs4 import BeautifulSoup #bs4 패키지에 있는 BeautifulSoup 기능을 쓰겠음
import lxml #파싱
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8' #url 주소를 변수에 저장
response = requests.get(url).text #url 변수에 저장한 url 주소를 requests 패키지로 get해 옴 -> response 변수에 저장
# print(response) 출력하면 응답되었는지 안되었는지 결과값 출력

#텍스트에서 정보를 추출
data = BeautifulSoup(response,'lxml') #정보 추출을 위해 BeautifulSoup을 통해서 문서 구조화, lxml파싱대신 html.parser써줘도 됨
money = data.select_one('#_cs_foreigninfo > div > div.api_cs_wrap > div > div.c_rate > div.rate_bx > div.rate_spot._rate_spot > div.rate_tlt > h3 > a > span.spt_con.dw > strong').text #선택자를 활용해서 해당 위치를 찾음
print(f'미국 환율은 money 입니다.')