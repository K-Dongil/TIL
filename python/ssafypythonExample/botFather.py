# 텔레그램으로 메세지 보내기
# id=1884153403
# https://api.telegram.org/bot1881066428:AAHGZvkEe2DHTr9tft5G4RRRzINiyrszr-E/ (기본주소)
# https://api.telegram.org/bot1881066428:AAHGZvkEe2DHTr9tft5G4RRRzINiyrszr-E/getMe (요청URL)
# https://api.telegram.org/bot1881066428:AAHGZvkEe2DHTr9tft5G4RRRzINiyrszr-E/getUpdates
# https://api.telegram.org/bot1881066428:AAHGZvkEe2DHTr9tft5G4RRRzINiyrszr-E/sendMessage?chate_id={}&text={}
    #기본 주소에 메서드가 붙음 (메서드:내가 조작할 내용)

import requests
'''
# 1. 사용자 정보 가져오기
# base-url/getUpdates로 요청 보내서,
# chat_id에 해당하는 값을 지정
'''
# 정보
token = '1881066428:AAHGZvkEe2DHTr9tft5G4RRRzINiyrszr-E'
base_url = f'https://api.telegram.org/bot{token}'

# url 요청하고, 결과를 python 자료구조로 저장
get_updates_url = f'{base_url}/getUpdates'
response = requests.get(get_updates_url).json()
chate_id = response['result'][0]['message']['chat']['id'] #1884153403

'''
# 2.메시지 보내기
# base_url/sendMessage?chat_id={위에서가져온값}&text={원하는 값}
#메세지 보내기
'''
# 0. 메세지 준비
import random
#메세지 입력 받아서 보내기 input()사용 
magic_number = random.sample(range(1,46), 6)
text = f'''
오늘의 로또 번호: {magic_number}
'''
send_message_url = f'{base_url}/sendMessage?chat_id={chate_id}&text={text}'

# 1. 요청
print(f'메세지 보낸 결과 : {response["ok"]}') #메세지 전송 성공 여부
requests.get(send_message_url) #request.get(url) -->메세지 쓰고 Enter