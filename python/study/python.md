## 파이썬 라이브러리

[doc.python.org]('https://docs.python.org/ko/3/library/index.html')

## 프로그래밍 언어 : 3형식

1. 저장
2. 조건
3. 반복

## 특징

- 특징
  1. 인터프리터 언어(Interpreter)
     - 소스 코드를 컴파일X, 한 줄씩 소스코드 읽어 바로 실행
     - 컴파일 언어에 비해 느릴 수 잇지만 빌드 과정 없이 바로 실행가능
  2. 객체 지향 프로그래밍
     - 파이썬은 모두 객체로 이뤄져 있음
  3. 동적 타이핑
     - 변수에 별도의 타입 지정이 필요 없음



## Python 개발환경

- 대화형 환경
  - Python 기본 Interpreter (IDLE Shell)
    - 인터프리터가 대화형 모드로 동작
      - 프롬프트(>>)에 코드를 작성하면 해당 코드가 실행 됨
      - 여러 줄의 코드가 작성되는 경우 보조 프롬프트(...)가 사용됨
    - Python이 설치된 환경에서는 기본적으로 활용 가능하나 디버깅 및 코드 편집, 반족 실행이 어려움
  - Jupyter Notebook
    - 웹 브라우저 환경에서 코드를 작성할 수 있는 오픈소스
    - 브라우저에서 코드를 실행하고 결과를 확인할 수 있음
  - 파이썬 쥬피터와 비쥬얼 스튜디오
    - 실시간으로 결과를 확인하며 학습하기 위함
  - 웹 : Visual Studio Code
    - HTML / CSS, Django, JavaScript, Vue 등 모두 개발하기 편한 환경
- 스크립트 실행
  - Python 스크립트 실행
    - IDE(ex - Pycharm), Text editor(ex - Visual Studio Code)등에서 작성한 파이썬 스크립트 파일을 직접 실행
  - .py 파일을 작성하고 IDE 혹은 Text Editor 활용



## 코드 스타일 가드

- 코드를 어떻게 작성할지 권장사항
  - 내가 작성하는 코드는 결국 다른사람들도 보게 되는 것 (맞춤법이라 생각)
- 파이썬 : PEP8
- 한글로 번역된 거 읽어보기



## 주석(Commnet)

- 한 줄 주석은 #으로 표현한다.
- 여러 줄의 주석은 한 줄씩 #을 사용하거나, """ 또는 '''표현한다.
  - docstring을 위해 사용
  - 함수/클래스의 설명을 작성 (설명서, 가이드라인)
  - 함수명.***doc\*** 출력하면 설명이 출력됨 (단 함수에 docstring을 설정해줘야 함)
- 주석할 코드 드래그 후 Ctrl + / 하면 주석처리



## 코드 라인

- 코드는 1줄에 1문장
- 문장은 파이썬이 실행 가능한 최소한의 코드 단위
- 세미콜론(;)을 사용하지는 않으나 한줄에 두개의 문장을 사용할 때 ;를 이용해 구분하여 표기가능



## 변수

- variable = 숫자, 문자, 객체 등 값을 넣을 수 있는 공간
- 사전적 의미 : "변화를 줄 수 있는" or  "변할 수 있는 수"
- 프로그래밍에서는 데이터를 담을 수 있는 공간(숫자, 문자, 객체)
- 변수 활용 이유 : 유지보수 관리 용이



#####  * 변수 선언하는 방법

- 변수명 = 대입할 값 (=는 대입)

- 변수는 할당 연산자(=)를 통해 값을 할당(assignment)

- 같은 값을 동시에 할당 가능

  ```python
  x = y = '값'
  x, y ='값1', '값2'
  ```

  ------

  ```python
  x, y = 1 #불가능
  ```



##### * 값 swap

- 임시변수 활용, Pythonic (x, y = y, x)



##### * 변수명 규칙

1.  영문자(대, 소문자 구분), 숫자, 언더바(_)를 사용할 수 있음.  ex)number와 Number는 다르다

2.  숫자로 시작할 수 없다. ex) 1a =0

3.  변수 하나에는 하나의 값만 넣을 수 있다.

   ​	- 어떤 값이 저장된 변수에 새로운 값을 넣으면 덮어씌워진다.
   
4.  길이 제한X, 대소문자 구별

5. 파이썬에서 이미 정의(예약)되고 있는 단어는 불가

   ex) Falase, True

   ```python
   import keyword
   print(keyword.kwlist) #를 통해서 사용되고 있는 예약어 확인가능
   ```

6. 내장함수나 모듈 사용X

   - 기존의 이름에 다른 값을 할당하게 되므로 더 이상 동작X

   ```python
   print('hi')
   print = 'hi' #print 함수에 hi 문자열을 저장해버림
   print('hi') #오류발생
   ```



##### * 데이터 타입

- 숫자 (int, float, complex)

- 문자열 (String)

- 참/ 거짓( Boolean)

- None

  *python에서는 오버플로가 일어나지 않는다. (메모리의 크기 자동 조정)



##### * 변수의 형태

- 숫자형 : 소수자 포함 숫자

  - float : 정수가 아닌 모든 실수

    - 314e - 2 = 3.14
    - float은 int로 형변환이 가능하나 소수점은 버려짐

  - 부동소수점에서 실수인경우 주의필요

    - 두 실수의 차이가 임의의 매우 작은 수(1e-10)보다 작은지를 확인, math 모듈 활용

    ```python
    abs(x - y) <= le-10  #le - 10는 사용자가 정한 임의의 수
    ```

    ```python
    # system상의 machine epslion
    import sys
    print(abs(x - y) <= sys.float_info.epsilon)
    ```

    ```python
    import math
    math.isclose(a, b)
    ```

  - 실수부와 허수부로 구성된 복소수는 complex 타입

    - 허수부는 j로 표현가능
    
  - round(값, 표현할 소수점자릿수) 

    -  round()는 0~4내림, 5 (짝수에서 5는 내림, 홀수에서 5는 올림)

- 문자열 자료형 :  'Hello, World!', "123"

  - 모든 문자는 str타입
  - 문자열은 작은 따옴표' or 큰 따옴표" 사용
    - 하나의 문장부호를 선택하여 유지

- 리스트 자료형 : [], [1, 3, 5] (묶음 자료형)

- 튜플 자료형 : (), (1, 2, 3) 읽기전용(수정불가) 묶음

- 딕셔너리 자료형:{'name':'MH',  'birth':'1118'}  클론(:)기준 왼쪽“키”, 오른쪽“값”

- 집합 자료형:set이용  교집합?합집합?여집합? set([1,2,3]), set("Hello")

- Boolean: True, False 참과 거짓 (논리자료형)

  - 계산식에 쓰일 때는 True는 1, False는 0으로 형변환
  - None, 빈 리스트, 빈 문자열 은 False, 이 외의 문자는 True
  - 값이 존재하는 리스트, 문자열  True

- None타입 : 값이 존재하지 않음

- type()

  - 변수에 할당된 값의 타입 확인

- 2진수 : 0b숫자

- 8진수 : 0o숫자

- 10진수 : 숫자

- 16진수 : 0x숫자



##### * 변수의 주소

- id()
  - 변수에 할당된 값(객체)의 고유한 아이덴티티 값이며, 메모리 주소를 확인
  - 변수에 저장된 값 == 사람, 메모리 주소 == 사람이 있는 위치(집)
  - 변수에 새로운 값을 초기화 시키면 주소도 바뀐다 (-5~ 256까지는 같음)



##### * 문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을 때

1. ""안에 '를 쓰기 or ''안에 "를 쓰기
2. \\' or \\"



##### * 이스케이프 문자

| 예약문자 | 내용(의미)       |
| -------- | ---------------- |
| \n       | 줄 바꿈          |
| \t       | 탭               |
| \r       | 캐리지리턴       |
| \0       | 널(Null)         |
| \\\\     | \                |
| \\'      | 단일인용부호(')  |
| \\"      | 이중인용부호('') |



##### * 타입 변환

- 파이썬에서 데이터 타입은 서로 변환 가능

- 암시적 타입 변환

  - 사용자 의도X, 파이썬 내부적으로 타입을 변환

  ```python
  True + 3 #True를 1로 변환해줌, 출력: 4
  5 + 5.0 #5를 float 타입으로 변환, 출력: 5.5
  5 + 5j + 5 #복소수로 바꿔줌, 출력: 10+5j
  ```

- 명시적 타입 변환

  - 사용자가 특정 함수를 활용하여 의도적으로 타입 변환
  - 형식에 맞아야 변환가능



##### * String Interpolation

- 변수의 값을 문자열의 자리표시자(placeholder)로 대체하는 방법

  - %-formatting

    ```python
    print('안녕, %s' % name) 
    ```

    ```
    print('안녕, %s %d' %(name, 5) 
    ```

  - str.format()

    ```python
    print('안녕, {}', format(name))
    ```

  - f-strings(python 3.6 버젼 이상)

    ```python
    pinrt(f'안녕, {name})
    ```

---

---

## 연산자

##### * 산술 연산자

- 기본적인 사칙연산 및 수식 계산

  | 연산자 | 내용     |
  | ------ | -------- |
  | +      | 덧셈     |
  | -      | 뺄셈     |
  | *      | 곱셈     |
  | /      | 나눗셈   |
  | //     | 몫       |
  | **     | 거듭제곱 |
  | %      | 나머지   |

- divmod(x, y)
  - 몫과 나머지를 출력
  - 튜플 형태로 반환



##### * 비교연산자

- 값을 비교하며, True/ False 값을 리턴

  | 연산자 | 내용                        |
  | ------ | --------------------------- |
  | <      | 미만                        |
  | <=     | 이하                        |
  | >      | 초과                        |
  | >=     | 이상                        |
  | ==     | 같음                        |
  | !=     | 같지않음                    |
  | is     | 객체 아이덴티티(OOP)        |
  | is not | 객체 아이덴티티가 아닌 경우 |

- 특정 변수가 비어 있는 확인 하기 위해서는 is None을 사용

  ```
  x = '비어있는가??'
  x is None
  #출력: False
  ```

  

##### * 논리연산자

- 일반적으로 비교연산자와 함께 사용

| 연산자  | 내용                           |
| ------- | ------------------------------ |
| A and B | A와 B 모두 True시, True        |
| A or B  | A와 B 모두 False시 ,False      |
| Not     | True를 False로, Flase를 True로 |

- ##### 결과가 확실한경우 두번째 값은 확인하지 않음

  - 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환

    - 0은 False, 0을 제외하고는 True

    - and연산에서 첫번째 값이 False인 경우 무조건 False -> 첫번째 값 반환

    - or 연산에서 첫번째 값이  True인 경우 무조건 True -> 첫번째 값 반환

    - 단축평가

      ```
      a = 10 and 5
      print(a) #출력5
      #10이 True이므로 5까지 비교하게 됨
      #만약 10대신 0이였다면 False이므로 뒤까지 볼 필요X 출력은 0
      
      b = 10 or 5
      print(b) #출력 10
      #첫번째 값이 True이므로 첫번째 값 무조건 출력
      
      c = 0 or 0 #출력은 0이나 뒤의 값이다.
      d = 0 or 5 #출력 5
      ```


##### * 복합 연산자

- 연산과 대입이 함께 이뤄짐
- +=, -=, *=, /=, //=, %= 등등



##### * Concatenation

- +는 숫자가 아닌 자료형에서도 사용가능

  - 리스트, 튜플, 문자열 사용 가능
  - range는 사용 불가능

- *는 숫자가 아닌 자료형에서도 사용가능

  - 리스트, 튜플, 문자열 사용 가능

  - range는 사용 불가능

    ```
    'hi' *3 #출력 : 'hihihi'
    (1, 2) * 3 #출력 : (1, 2, 1, 2, 1, 2)
    ```

    

- 컨테이너(데이터 타입), OOP에서 연산자의 다양한 활용을 확인



##### *  Concatenation Test

- 특정 요소가 속해 있는지 여부를 확인

  ```
  'b' in 'apple'
  #출력: False
  ```



##### * Identity

- is 연산자를 통해 동일한 객체(object)인지 확인 가능함



##### * Indexing / Sliciing

- []를 통해 값을 접근하고, [:]를 통해 슬라이싱 가능함
- 문자열은 0부터 Indexing번호를 가진다.
- Indexing : 리스트, 튜플, range, 문자열 사용 가능
- Sliciing : 리스트, 튜플, range, 문자열 사용 가능
  - [x:y]일 때 x포함 y불포함 



##### *연산자 우선순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 `**`
5. 단항연산자 `+`, `-` (음수/양수 부호)
6. 산술연산자 `*`, `/`, `%`
7. 산술연산자 `+`, `-`
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `o`

```
print(-3 ** 6) # 출력 : -729
print((-3) ** 6) # 출력 : 729
```



---

---

## 표현식(Expression)/문장(Statement)

- 표현식
  - 하나의 값(value)으로 환원(reduce)될 수 있는 문장을 의미
  - 값이 평가되고 있는 부분
    - ex) x  < 100
  - 식별자(변수명), 값, 연산자로 구성
  - 표현식은 평가(evaluate)되고, 값으로 변경
  - 하나의 값으로 환원(reduce)될 수 있는 문장
    - 식: 값이 될수 있냐 없냐?
  -  표현식 => evaluate => 값
    - 표현식은 결과적으로 값이 나온다.
    - 표현식에 함수호출(값을 return해주는 함수)이 올 수도 있다.
  - 하나의 값(value)도 표현식이 될 수 있다
- 문장
  - 값, 표현식
  - 파이썬이 실행가능한 최소한의 코드 단위
  - 모든 표현식은 문장
    - 표현식이 아닌 문장이 존재
      - ex) del5
  - 

```
if a > 3:
	실행문장
위에서 if a > 3:는 조건문
		a > 3 는 조건식
```

![image-20210719195044900](python.assets/image-20210719195044900.png)



---

---

## 컨테이너(데이터 타입?)

![image-20210720151951163](python.assets/image-20210720151951163.png)



- 컨테이너 : 여러 개의 값을 저장할 수 있는 것(객체)
  - 시퀀스형, 비 시퀀스형
  - string, list, tuple, range, set, dictionary
- 시퀀스(sequence)형 : 순서가 있는(ordered) 데이터
  - 순서가 있다 != 정렬되어 있다
  - 특정 위치의 데이터를 가리킬 수 있다.
  - 리스트(list), 튜플(tuple), 레인지(range), 문자형(string), 바이너리(binary)
  - 데이터의 길이(갯수) : len()
    - 시퀀스(문자열, 바이트열, 튜플, 리스트, range) 또는 컬렉션(딕셔너리, 집합 또는 불변 집합)
  - 최소/최대 : min(), max()
    - 문자열은 ascii 코드에 따름
  - 시퀀스에서의 특정 원소의 개수 : .count(찾고 싶은 원소)
    - 시퀀스에 등장하지 않는 경우 0 반환
  - 시퀀스 포함 여부 확인
    - in, not in
  - indexing : s[ i ]
  - slicing : s[ i : j ]
- 비 시퀀스형 : 순서가 없는(unordered) 데이터
  - 세트(set), 딕셔너리(dictionary)

### 1. 시퀀스

##### *리스트

- 리스트는 순서가 있는 시퀀스로 인덱스를 통해 접근
  - (시퀀스: 순서가 있다. But 정렬X)
  
- 인덱스는 0부터 시작

- 대괄호[] 혹은 list()를 통해 생성

- 값에 대한 접근은 list[숫자]

- 서로 다른 타입의 데이터를 저장할 수 있다.

- 리스트 오름차순 정렬

  ```
  numbers = [
           85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
           51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
           52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
       ]
  
  # 아래에 코드를 작성하시오.
  
  number = []
  min_num = 0
  for i in range(len(numbers)):
      for j in range(i+1, len(numbers)):
          if numbers[i] < numbers[j]:
              pass
          elif numbers[i] > numbers[j]:
              min_num = numbers[i]
              numbers[i] = numbers[j]
              numbers[j] = min_num
  print(numbers)
  ---
  numbers = [
           85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
           51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
           52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
       ]
  
  # 아래에 코드를 작성하시오.
  
  number = []
  min_num = 0
  for i in range(len(numbers)):
      for j in range(i+1, len(numbers)):
          if numbers[i] > numbers[j]:
              min_num = numbers[i]
              numbers[i] = numbers[j]
              numbers[j] = min_num
  print(numbers)
  ---
  numbers = [
           85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
           51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
           52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
       ]
  
  # 아래에 코드를 작성하시오.
  
  number = []
  min_num = 0
  for i in range(len(numbers)):
      for j in range(i+1, len(numbers)):
          if numbers[i] < numbers[j]:
              pass
          elif numbers[i] > numbers[j]:
              min_num = numbers[i]
              numbers[i] = numbers[j]
              numbers[j] = min_num
          if j == len(numbers) - 1:
              number.append(numbers[i])
  print(number)
  ```

  



##### *튜플

- 튜플은 수정 불가능한(immutable) 시퀀스로 인덱스로 접근

- 소괄호() 혹은 tuple()을 통해 생성

  - 값이 하나인 튜플은 값 뒤에 쉼표를 붙여줘야 함

    ```
    a = (1, )
    print(type(a)) #출력: tuple
    ```

- 값에 대한 접근은 tuple(숫자)

- 일반적으로 파이썬 내부에서 활용

  - multiple assignment
  - 추후 함수에서 복수의 값을 반환하는 경우에도 활용 (변경 불가능 특징 때문에)
  - 값 swap은 가능



##### *range

- range는 숫자의 시퀀스를 나타내기 위해 사용
  - 기본형 : range(n)
    - 0부터 n-1까지의 숫자의 시퀀스
    - 갯수는 n개
  - 범위 지정 : range(n, m)
    - n부터 m-1까지의 숫자의 시퀀스
  - 범위 및 스텝 지정 :  range(n, m, s)
    - n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스

```
range(4) #출력 : range(0, 4) 0,1,2,3이 들어있음
list(range(4)) #출력 : [0, 1, 2, 3] list로 형변환해서 출력
print(type(range(4))) #출력 : range
```

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

### 2. 비 시퀀스

##### * 세트

- 순서가 없는 자료구조
  - 중괄호{} 혹은 set()을 통해 생성
    - 빈 세트를 만들기 위해서는 set()을 반드시 활용
    - 빈 중괄호는 딕셔너리!!
  - 순서가 없어 별도의 값에 접근할 수 없음
- 수학에서의 집합과 동일한 구조를 가짐
  - 집합 연산이 가능
  - 중복된 값이 존재X
    - 만들 때 중복된 값이 존재하면 중복 값 제거한다.
- 활용 가능 (집합)연산자 : 차집합, 합집합, 교집합
  - 차집합 : -
  - 합집합 : |
    - 합칠 때 중복 제거
  - 교집합 : &

- 세트를 활용하면 다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음
  - 단, 이후 순서가 무시되므로 순서가 중요한 경우 사용X



##### * 딕셔너리 {key : value}

- key와 value가 쌍으로 이뤄진 자료구조
  - 중괄호{} 혹은 dict()을 통해 생성
  - key를 통해 value에 접근
- key와 value가 쌍으로 이뤄진 자료구조
  - key는 변경 불가능한 데이터(immutable)만 활용 가능
    - string, integer, float, boolean, tuple, range
  - value는 모든 값으로 설정 가능(리스트, 딕셔너리 등)



### 3. 변경 불가능(immutable)한 데이터

- 리터럴(literal) - 숫자(Number), 문자열(String), 참/거짓(Bool)
- range
- tuple
- 변경 불가능한 데이터의 복사
  - 공유X ,재할당
  - b = a를 하면 같은 값이 공유

### 4. 변경 가능(mutable)한 데이터

- list, set, dictionary
- 변경이 가능한 데이터를 복사하면 주소를 공유
  - 동일한 리스트(객체)의 주소를 참조



![image-20210720151717178](python.assets/image-20210720151717178.png)



---

---

## 제어문

- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요
- 제어문은 순서도(flow chart)로 표현가능
- 순차적인 코드의 흐름을 제어하는 것을 제어문이라고 하고, 제어문은 크게 **조건문**과 **반복문**



### 1. 조건문(Conditional Statement)

- if문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

  - if <expression>:

    ​	# Code block (문장들의 block)

  - expression에는 참/거짓에 대한 조건식

  - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블록을 실행

  - 이외의 else 이후 들여쓰기 되어있는 코드 블록을 실행

    - else는 선택적으로 활용 가능함

  - if의 조건식이 참이면 이 후 조건문(elif, else)문은 실행X

    - 조건식이 거짓이면 바로 다음의 조건문 실행

- if, elif, else는 순차적으로 실행된다.
- 중첩 조건문(Nested Conditional Statement)
  - 조건문은 다른 조건문에 중첩되어 사용 될 수 잇음 (들여쓰기 유의)
- 조건 표현식(Conditional Expression)
  - 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용
  - 삼항 연산자(Ternary Operator)로 부르기도 함
  - <true인 경우 값> if < expression> else <false인 경우 값>



### 2. 반복문(Loop Statement)

- while문

  - 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함

  - 조건식이 참인 경우 반복적으로 코드를 실행(조건이 False가 될때까지 반복)

  - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행

  - 무한 루프를 하지 않도록 종료 조건이 반드시 필요

  - while <expression> :

    ​	# Code block
    
  - EOF : End Of File

    - 더이상 읽을 자료가 없다는 뜻
    - try except으로 오류 해결가능

- for문

  - 반복 가능(iterable)한 객체를 모두 순회하면 종료(별도의 종료 조건이 필요 없음)

  - for문은 시퀀스(string, tuple, list, range)를 포함한  iterable한 객체 요소를 모두 순회함

    - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건 필요X

  - for <임시변수> in <순회가능한 데이터(iterable)>:

    ​	# Code block

    - for 문 안에서 임시 변수에 다른 값을 할당해도 반복구문에 영향을 주지 않습니다.

      ```
      for i in range(10):
      	print(i)
      	i = 5
      ```

      

  - iterable한 객체에서 차례대로 변수에 담겨져서 Code block이 실행되며 순회한다.

  - 변수명을 단수형 itreable에는 복수형을 이용해서 쓰자

    - 문자열도 iterable가능한 데이터다
    
    ```
    chars = 'happy'
    for char in chars:
    	print(char)
    #출력:
    h
    a
    p
    p
    y
    ```

- 반복 제어

  - break, continue, for-else
  - break : 반복문을 강제종료
  - continue : continue 아래 있는 block(코드) 실행X, 다음 반복을 수행
  - for-else : 끝까지 반복문을 실행한 이후에 else문 실행
    - break를 통해 중간에 종료되는 경우 else문은 실행X
    
    - for-else에서 else는 for랑 연관이 있다
    
      - 간혹 for문 안에 if가 있을 때 주의!!
    
      ```
      for i in range(10):
          print(i)
          if i == 100:
              print(f'{i}에서 break 실행됨.')
              break
      else:
          print("break 실행안됨.")
      0
      1
      2
      3
      4
      5
      6
      7
      8
      9
      break 실행안됨.
      ```
    
      

- pass문

  - 아무것도 하지 않음

    - 특별히 할 일이 없을 때 자리를 채우는 용도로 사용

      - 문법적으로 오류나는 것을 방지할 때

      ```
      for i in rage(5):
      	if i == 3:
      		pass
      	print(i)
      ```

    - 반복문 아니여도 사용 가능

- enumerate()

  - enumerate(순회가능한 데이터(iterable))
    - index와 (순회가능한 데이터에서 index맞는 위치의 데이터)
  - index와 value를 함께 활용 가능
  - enumerate() 에 의해 반환되는 인덱스가 0으로 시작
    - 인덱스가 1로 시작할 수 있음
      - enumerate(순회가능한 데이터(iterable), 1)

- ex 1) 

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
  
#리스트 순회하기 -enumerate
members=['a', 'b', 'c']
for i, member in enumerate(members):
	print(i, member)
```

- ex 2) lunch_box를 다 돌기

```python
# 리스트를 모두 반복하는 법 (for)

lunch = ['햄버거', '피자', '치킨']
for lunch in lunch_box:
	print(lunch)
```

→ lunch라는 변수에 계속 햄버거 피자 치킨 순서로 넣어주는 것

- ex 3) lunch_box의 길이만큼 돌기_len

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



---

---























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