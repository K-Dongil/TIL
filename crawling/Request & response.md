## Request & response

##### * web

- web(world Wid Web)
  - 인터넷에 연결된 컴퓨터를 통해 사람들이 정보를 공유할 수 있는 전 세계적
  - 컴퓨터간의 정보공유 (요청와 응답으로 이뤄져 있음)

- 웹의 구성 요소(mdn)
  - HTTP 프로토콜이 서버와 클라이언트간의 데이터 전송을 관리
  - URL을 통해 클라이언트는 웹 요소에 접근
  - HTML 같은 웹 문서를 작성



##### * HTTP

- HTTP는 HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
- 웹에서 이뤄지는 모든 데이터 교환의 기초이며, 클라이언트  - 서버 프로토콜
- 요청(reuqests)
  - 보통 브라우저인 클라이언트에 의해 전송되는 메시지
- 응답(response)
  - 서버에서 응답으로 전송되는 메시지

- 클라이언트는 URL을 통해 요청하고, 서버는 문서(텍스트)를 응답한다
- 가장 대표적인 클라이언트 프로그램 : 브라우저(엣지, 크롬)
- 가장 대표젹인 서버 프로그램(응답) : 네이버, 구글, 깃헙



##### * requests (HTTP library for python)

- 또 다른 클라이언트 프로그램
- 서버에 요청하여 HTML문서를 받는다
- requests의 역할은  HTML을 받아오는 것까지 원하는 대로 사용하기 위해 추가적인 작업이 필요

1. pip install requests 
   - 패키지 설치
2. import requests 
   - requests 모듈 불러오기
3. url = '정보를 가지고올 url주소를 담는다' 
   - 요청을 보낼 URL
4. response = requests(요청을 보낼건데 ).get(받을거다).(url)(어디서)
   - 실제 요청을 보내고, 응답 객체를 response 변수에 저장



##### * BeautifulSoup

- HTML에서 데이터를 뽑아 주는 라이브러리

1. pip install beautifulsoup4

2. from bs4 import BeautifulSoup

3. BeautifulSoup(response.text, 'html.parser')

   - response.text (응답 객체의 본문을 text형식으로)

   - 컴퓨터(프로그램)이 해석할 수 있게 parser작업 : 응답 객체의 본문(text)을 해석

4. BeautifulSoup(response.text, 'html.parser').selete_one('css selector')

   - select_one 메서드 인자로 원하는 정보의 css selector를 집어넣으면 요소를 가져온다
     - 요소 :  태그의 처음부터 끝
   - 해석한 data에서 원하는 정보를 선택

5. BeautifulSoup(response.text, 'html.parser').selete_one('css selector').text

   - 요소에서 값만 가져오기



##### * 크롤링(Crawling)

- 일반적인 웹 서버는 HTML(문서양식)을 응답으로 전송
  - HTML : 브라우저를 통해 화면 구성

1. 요청을 보낼 URL
2. 실제 요청을 보내고, 응답 객체를 response 변수에 저장
3. 응답 객체의 본문(text)을 해석하여 data변수에 저장
4. 해석한 data에서 원하는 정보를 선택하고, 내용만 kospi에 저장

- 단점 
  - 브라우저가 아닌 상황에서 필요 없는 데이터가 너무 많음
  - 원하는 데이터를 얻기 위한 추가작업



