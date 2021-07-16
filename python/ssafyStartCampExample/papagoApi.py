# '''
# 1. 랜덤 명언을 가져와서 변수에 저장
# https://favqs.com/api/qotd
# '''

# import requests
# # 0. URL
# url = 'https://favqs.com/api/qotd'

# # 1. 요청을 보내서 응답받은 JSON을 파이썬 자료구조로
# response = requests.get(url).json()

# # 2. 해당 내용에서 필요한 부분 꺼내기
# print(response['quote']['author'])
# print(response['quote']['body'])
# quote_body = response['quote']['body']
# '''
# 2.해당 명언의 내용을 네이버 API를 통해서 papago 번역 결과를 가져온다.
# https://openapi.naver.com/v1/papago/n2mt
# 필수 파라미터 : source=en, target=ko, text
# '''
# # 0. naver에서 발급받은 ID/secret
# headers = {
#     'X-naver-Client-Id' : 'orXNu42lU1emSAstK__G',
#     'X-naver-Client-Secret' : 'H9dvk1fWJI'
# }

# # 1. URL
# source = 'en'
# target = 'ko'
# text = quote_body
# data = {
#     'source' : source,
#     'target' : target,
#     'text' : text
# }
# url = f'https://openapi.naver.com/v1/papago/n2mt?source={source}&target&text={text}'
# print(url)

# # 2. 요청을 보내서 응답받은 JSON을 파이썬 자료구조로
# response = requests.post(url, headers=headers, data=data).json() #requests.post -> post방식으로 url 가져온다

# # 3. 해당 내용에서 필요한 부분 꺼내기
# print(text)
# print(response)

'''
1. 랜덤 명언을 가져와서 변수에 저장
https://favqs.com/api/qotd
'''
import requests
# 0. URL
url = 'https://favqs.com/api/qotd'
# 1. 요청을 보내서 응답받은 JSON을 파이썬 자료구조로
response = requests.get(url).json()
# 2. 해당 내용에서 필요한 부분 꺼내기
print(response['quote']['author'])
quote_body = response['quote']['body']
'''
2. 해당 명언의 내용을 네이버 API를 통해서
papago 번역 결과를 가져온다.
POST https://openapi.naver.com/v1/papago/n2mt
필수 파라미터 : source=en, target=ko, text 
'''
# 0. naver에서 발급받은 ID/secret
headers = {
    'X-Naver-Client-Id': 'orXNu42lU1emSAstK__G',
    'X-Naver-Client-Secret': 'H9dvk1fWJI'
}
# 0. URL
source = 'en'
target = 'ko'
text = quote_body
data = {
    'source': source,
    'target': target,
    'text': text
}
url = f'https://openapi.naver.com/v1/papago/n2mt'
# 1. 요청을 보내서 응답받은 JSON을 파이썬 자료구조로
response = requests.post(url, headers=headers, data=data).json() #requests.post -> post방식으로 url 가져온다
# 2. 해당 내용에서 필요한 부분 꺼내기
print(text)
print(response['message']['result']['translatedText'])