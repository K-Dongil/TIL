import requests
#1. url 요청을 보내서 저장
url = 'https://api.nationalize.io/?name=michael'
response = requests.get(url)
print(response)
#2. json()을 통해서 파이썬 자료구조화
result = response.json()
print(result)
#3.내가 원하는 값 출력
#딕셔너리 -> key로 접근 (country)
print(result['country'])
#결과가 리스트 ->index로 접근
print(result['country'][0])
#결과가 딕셔너리 -> 내가 원하는 값은 US니까, key로 접근
print(result['country'][0]['country_id'])


# import requests
# name = ['tak', 'tony', 'eric']
# url = 'https://api.nationalize.io/?name='
# for i in name:
#     response = requests.get(url+i)
#     result = response.json()
#     result2 = result['country']
#     print(i,' : ',result2[0])