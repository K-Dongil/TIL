## 변수

- variable = 숫자, 문자, 객체 등 값을 넣을 수 있는 공간
- 사전적 의미 : "변화를 줄 수 있는" or  "변할 수 있는 수"
- 프로그래밍에서는 데이터를 담을 수 있는 공간(숫자, 문자, 객체)

#####  변수 선언하는 방법

- 변수명 = 대입할 값 (=는 대입)

##### 변수명 규칙

1. 영문자(대, 소문자 구분), 숫자, 언더바(_)를 사용할 수 있음.  ex)number와 Number는 다르다

2. 숫자로 시작할 수 없다. ex) 1a =0

3. 변수 하나에는 하나의 값만 넣을 수 있다.

   ​	- 어떤 값이 저장된 변수에 새로운 값을 넣으면 덮어씌워진다.

##### 변수의 형태

- 숫자형 : 소수자 포함 숫자
- 문자열 자료형 :  'Hello, World!', "123"
- 리스트 자료형 : [], [1, 3, 5] (묶음 자료형)
- 튜플 자료형 : (), (1, 2, 3) 읽기전용(수정불가) 묶음
- 딕셔너리 자료형:{'name':'MH',  'birth':'1118'}  클론(:)기준 왼쪽“키”, 오른쪽“값”

- 집합 자료형:set이용  교집합?합집합?여집합? set([1,2,3]), set("Hello")

- Boolean: True, False 참과 거짓 (논리자료형)

##### 문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을 때

1. ""안에 '를 쓰기 or ''안에 "를 쓰기
2. \\' or \\"

## for문

```py
# 반복문 while 
'''
종료조건을 생각하자.
0 -> 1 -> 2 (값 초기화를 0, 3보다 작을 때까지)
'''
# 1) 값 초기화
n = 0
while n < 3:
  print('안녕하세요.')
  n += 1
  # n = n + 1

# 반복문 for문
'''
정해진 것을 반복!
정해진 것을 만들어야만 한다...
길이가 3이여야한다. (총 3번이니까)
'''
for i in range(3):
  print('hi!')

# 리스트를 모두 반복하는 법(for)
lunch_box = ['햄버거', '피자', '치킨']

# 1) lunch_box를 다 돌기
for lunch in lunch_box:
  # lunch = ....
  print(lunch)

# 2) lunch_box의 길이를 바탕으로 0부터 하나씩 접근하기
for i in range(len(lunch_box)):
  print(lunch_box[i])
```

## range

```py
# range 기본
range(5)
range(0, 5) # => 0, 1, 2, 3, 4?????
print(range(5)) # => range(0, 5)
print(list(range(5))) # => [0, 1, 2, 3, 4] / 내용을 보려면 list로 바꿔서!

a = range(1000)
b = list(range(1000))
print(a)
print(b)
```

- range(?,?) 와 list(range(?,?)) 차이
  - http://pythontutor.com/visualize.html#code=a%20%3D%20range%281000%29%0Ab%20%3D%20list%28range%281000%29%29&cumulative=false&curInstr=2&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

## 프로그래밍 언어 : 3형식

1. 저장
2. 조건
3. 반복

### **변수 활용 이유**

⇒ 유지보수 관리가 용이함

## 딕셔너리 {key : value}

```python
dust = {'영등포구':58, '강남구':40}
print(dust['영등포구']) = 58
```

# 반복문

- **while** : 조건이 True인 동안 반복적으로 실행 **종료조건이 반드시 필요**
- **for** : 정해진 범위를 반복하기에 **종료조건 필요없음**

```python
for i in range(3): 
	print('hello')
```

→ 3번 반복

## 1) lunch_box를 다 돌기

```python
# 리스트를 모두 반복하는 법 (for)

lunch = ['햄버거', '피자', '치킨']
for lunch in lunch_box:
	print(lunch)
```

→ lunch라는 변수에 계속 햄버거 피자 치킨 순서로 넣어주는 것

## 2) lunch_box의 길이만큼 돌기_len

```python
for i in range(len(lunch_box)):
	print(lunch_box[i])
#range(5)
# 숫자가 0부터 4까지
print(range(5))
print(list(range(5))
print(range(0,5))
#리스트 길이가 5
# 인덱스? 0,1,2,3,4!

# 1이상 46 미만!
print(range(1,46))
```

# 함수

: 특정한 용도의 동작하는 코드를 한 곳에 모아 놓은 것 (**재사용성**)

```python
print(1+3)

# abs(-3) ⇒ 3 절대값 absolute value
# len('hi') ⇒ 2 길이 length
```

## Random함수 import하기

### 1) Random.sample

→  random.sample(리스트, 개수)

→ 리스트에서 특정 수의 요소를 임의적으로 비복원추출

ex) random.sample(numbers,6)

### 2) Random.choice

→ random.choice(리스트)

→ 리스트에서 임의로 하나의 요소를 선택

ex) random.choice(menu)

```python
import random
menu = ['롯데리아','홍콩반점','김밥천국']
choice = random.choice(menu)

print(choice)
# 변수명이 lunch box인 리스트를 만들어주세요
lunch_box = ['파스타', '피자', '치킨']
#점심 메뉴 최소 3개 이상 작성해주세요.
print(lunch_box)

# 1. random 모듈을 가져온다.
import random

# 2. lunch_box 에서 하나를 선택하여, menu 변수에 저장한다.
menu = random.choice(lunch_box)

# 3. menu 변수를 출력한다.
print("메뉴 : " + menu)
```

→ random으로 선택을 할 건데, lunch_box 중에서 그것을 menu에 저장

```python
menu2 = range(1,46)
pick = random.sample(menu2, 4)
print(pick)
```

### 로또 실습하기

```python
# 아래에 코드를 작성하세요.

# 1. 필요한 모듈을 불러오세요.
import random
# 2. 1~45까지 숫자를 numbers에 저장하세요.
numbers = range(1,46)
# 3. numbers 중에 6개의 숫자를 뽑아 lucky에 저장하세요.
lucky = random.sample(numbers,6)
# 4. lucky를 출력하세요.
print(lucky)
```

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3a915057-413a-40b9-a253-34c0f82078fb/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3a915057-413a-40b9-a253-34c0f82078fb/Untitled.png)

## 정렬기능 sorted

```python
print(sorted(lucky)) # 정렬해줌 
```

## range(1000) vs list(range(1000))

```python
print(list(range(5))) #-> [0,1,2,3,4]

a = range(1000)
b = list(range(1000))
print(a)
print(b)
```

## 파이썬 내에서 json 구조 정렬하기

- pprint.pprint(json구조 담긴 변수)

## 문자열 길게 쓸 때

- """ """

## f-string



## 기본주소와 메서드

- 기본주소에 메서드가 붙은 것 : 내가 조작할 내용

```
# https://api.telegram.org/bot1881066428:AAHGZvkEe2DHTr9tft5G4RRRzINiyrszr-E/ (기본주소)
# https://api.telegram.org/bot1881066428:AAHGZvkEe2DHTr9tft5G4RRRzINiyrszr-E/getMe (요청URL)
```



## 배포

- pythonanywhere (https://www.pythonanywhere.com/) 
- heroku
- Amazon Web Service (AWS EC2)

![image-20210716160400694](python.assets/image-20210716160400694.png)

## Flask

- pythonanywhere에서 Files-> mysite/ flask_app.py에서 실습하였음.

```
# 응답
# 사용자가 요청 보낼 URL 패턴 만들고
@app.route('/lotto') #주소
#함수를 만들어서
def hello_world():
    pick = random.sample(range(1,46), 6)
    return f'{pick}' #반환하는 것
```

- 위에 코드에서의 웹 주소 : http://kdongil1569.pythonanywhere.com/lotto 
  - app.route에 적는 부분이 http://kdongil1569.pythonanywhere.com 에 추가된다.
  - kdongil1569는 플라스크에서 ID부분





## 참고

(https://hphk.notion.site/3-cc150ad7c7db47a2a27c9bfe35199075)

(https://github.com/edutak/TIL-gj)

(https://www.notion.so/ff144edf41044fb789ea4c3e7b478fe8?v=38e1799d52724a269df8b4252e7684a3)