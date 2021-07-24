import requests #requests 패키지 import
import pprint #pprint 패키지 import
url = 'https://www.metaweather.com/api/location/1132599/' #json이 저장된 url주소를 변수에 담아 줌
response = requests.get(url).json() #reuqests.get(get방식으로 url 가져온다)을 이용하여 url가져오는데 json형태로 가져옴
#pprint.pprint(response) << 출력하면 json형태가 결과창에 뜸
weather = [] #리스트 생성
for i in range(len(response['consolidated_weather'])): #위에서 가져온 json에서 consolidated_weather를 가져오면 리스트 형식임
    weather.append(response['consolidated_weather'][i]['weather_state_name']) #리스트에 i번째 날 날씨 추가
    if i==(len(response['consolidated_weather'])-1):
        for i in range(len(response['consolidated_weather'])):
            print('{}일 뒤 날씨: {}'.format(i, weather[i]))

#================================================================================
# import requests
# from datetime import datetime
# url = 'https://www.metaweather.com/api/location/1132599/' + str(datetime.today().year) + '/'+str(datetime.today().month) + '/'+str(datetime.today().day+2) + '/'
# response = requests.get(url).json()
# weather = response[0]['weather_state_name']
# trans = {
#     'Snow': '눈',
#     'Sleet' : '진눈깨비',
#     'Hail' : '우박',
#     'Thunderstorm' : '뇌우',
#     'Heavy Rain' : '폭우',
#     'Light Rain' : '가벼운 비',
#     'Showers' : '소나기',
#     'Heavy Cloud' : '구름많음',
#     'Light Cloud' : '구름조금',
#     'Clear' : '맑은'
# }
#print(day['weather_state_name']) #이런 식으로 번역 결과를 가져온다
#print(trans['Light Rain']) #'Light Rain'
#print(trans[day['weather_state_name']]) #코드를 이렇게?

# print(f'서울의 모레 날씨는 {trans[weather]}입니다.')
#================================================================================

# #0 import 항상 최상단에 작성을 하자
# import requests
# from requests.models import Response

# #1. URL에 파이썬으로 요청
# url = 'https://www.metaweather.com/api/location/1132599'

# #Json 형식을 파이썬 자료구조 변형(.json())
# result = requests.get(url).json()
# print(result)

# #3. 원하는 값을 추출
# print(result['consolidated_weather'])
# print(type(result['consolidated_weather'])) #자료구조 파악이 잘 안되면 하나하나 찍어보자 

# #4. 첫번째 데이터
# print(type(result['consolidated_weather'][0]))

# day1 = result['consolidated_weather'][0]

# print(f'최고기온은 {day1["max_temp"]}')

# print(f'''{day1['applicable_date']} : {day["weather_state_name"]}
# 최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}
# ''') 

# #5. 무엇을 반복해야하는가? result['consolidated_weather']!!!
# for day1 in result['consolidated_weather']:
#     print(f'''{day1['applicable_date']} : {day["weather_state_name"]}
#     최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}
#     ''') 