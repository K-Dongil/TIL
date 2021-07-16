## 웹 크롤링

- 브라우저를 통해 사용하던 웹 문서(HTML)를 파이썬으로 요청

- 프로그래밍을 통해 정보 수집하기

- BeautifulSoup으로 웹 문서 구조형태로 변형

- 선택자를 활용하여 원하는 데이터 활용

1. 크롤링에 필요한 라이브러리 설치
2. import로 라이브러리 가져오기
3. 데이터 가져올 url 변수에 저장
4. requests 패키지로 url get
5. 4번을 변수에 담아서 출력해보기 : 응답여부 확인
6. 파싱하기 (lxml, html.parser)
7. 정보 추출을 위해 BeautifulSoup을 통해서 문서 구조화
8. css selector을 이용해서 특정 값 추출 

## vs code에서 패키지 설치하기

Terminal > bash창에서 

##### requests 설치

requests 패키지로 변수에 담은 url주소 get함

```py
$ pip install requests
```

##### bs4 설치 

정보 추출을 위해 BeautifulSoup을 통해서 문서 구조화

```
$ pip install bs4
```

##### lxml 설치

파싱

``````
$ pip install lxml
``````



## css selector 가져오기

1. 홈페이지에서 오른쪽 클릭
2. 검사
3. 가져올 데이터 값에서 오른쪽 클릭
4. Copy
5. css selector



## 예제

```python
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
```

