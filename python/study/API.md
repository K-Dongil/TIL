## API

- 실시간 업데이트 되는 정보를 활용하기 위한 데이터 형식
- 응용 프로그램에서 사용할 수 있도록, 운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스
  - 응용 프로그램을 위한 접점
- 데이터를 교환하기 위한 JSON파일을 파이썬으로 요청
- JSON을 쉽게 파이썬 문법으로 변형, JSON구조 (딕셔너리 +리스트 구조)
  - 가져온 것은 string형태이므로 json으로 parser해줘야함
- 데이터 구조를 활용하여 원하는 데이터 활용(나중에 요청을 통해 특정 기능을 제어)



##### * API Server

- 응용 프로그램(개발자)를 위한 데이터를 응답하는 프로그램



##### * API 서버로부터 데이터 받아보기

1. pip install requests
   - 패키지 설치
2. import reuqests
   - requests 모듈 불러오기
3. url = 'api가 담겨있는 주소' 
   - 요청을 보낼 URL - json형태로 data가 있는 url주소)
4. requests.get(url)
5. requests.get(url).json()
   - 가져온 것은 string형태이므로 json으로 parser해줘야함





TMDB