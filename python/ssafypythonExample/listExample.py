#로또 번호 
#코드 실행은 python 파일명 .py
#1.random 모듈을 가져오기
import random
#2. numbers 통(리스트) 만들기
numbers = list(range(1,46))
#3. random에서 sample을 6개 하고, pick에 저장하고
pick = random.sample(numbers, 6)
#랜덤모듈의 sample함수를 numbers에서 6개 뽑게끔 명령
#4. pick 출력
print(pick)
