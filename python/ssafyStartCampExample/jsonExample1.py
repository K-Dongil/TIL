#요청 보내주는 requests를 가져온다.
import requests

#1. url로 요청을 보낸 결과를 저장한다.
url = 'https://api.agify.io?name=michael'

#저장하는데, 이거 json이라서 리스트-딕셔너리 구조로 바꿔줘!
response = requests.get(url).json() #JSON 데이터는 이렇게 쓰면 파이썬 자료구조로 바꿔준다
print(response)
print(type(response))

#저장하는데, 이거 text로 바꿔줘!
# response = requests.get(url).text() 텍스트
# print(response)
# print(type(response)) str형태

#===========================================================================
# import requests
# # name = input('영문 이름 입력: ')
# names = ['tak', 'tony', 'eric', 'musk']
# # url = f'https://api.agify.io?name={name}&country_id=KR'
# url = 'https://api.agify.io?'
# for name in names:
#     url += f'name[]={name}&'
# print(url)
# responses = requests.get(url).json()  # json() -> dict 형식으로 변환
# for response in responses:
#     age = response.get('age')
#     name = response.get('name')
#     print(name, age)