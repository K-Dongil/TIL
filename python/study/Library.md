## 알고리즘 풀면서 도움되는 함수

##### * map()

- 리스트와 같은 시퀀스형 자료의 모든 원소에 동일한 연산/ 기능을 적용시킬 때 사용

- map(x, y) 
  - x : 함수
  - y :시퀀스형 자료
- map함수 사용 시 결과값을 리스트 형태로 반환하고 싶다면 리스트로 형변환을 해야한다.

##### * split()

- 특정 문자 기준으로 문자열을 분리해 리스트 안에 넣어준다
- 괄호 안에 값이 없을 시 공백을 기준으로 문자열 분리



##### * sys

- sys.stdin.readline()
  - input()보다 빠르게 입력받음

- 한 줄 단위로 입력받아 개행문자까지 같이 입력 받아진다.

  - Enter를 치면 \n으로 입력받는다. --> sys.stdin.readline()을 변수에 저장하면 개행문자 \n까지 같이 저장되어진다

    - sys.stdin.readline()로 입력된 값을 변수에 저장하여 print()로 출력했을 때는 개행문자가 껴있는지 확인할 수 없다.

      - python의 print는 \n이 기본값이기 때문

      - 하지만 if문을 통해 개행문자 확인가능

        ```
        a = sys.stdin.readline()
        #입력을 5로 받았다 가정
        print(a) # 출력 : 5
        if '\n' in a: # 개행문자 \n이 a안에 있다면
        	print('개행문자 포함되어 있다.')
        else: # 개행문자 \n이 a안에 없다면
        	print('개행문자 불포함 되어있다.')
        
        # 위의 결과값으로는 개행문자 포함되어 있다.가 출력된다
        ```

  - split()을 쓸 때는 개행문자가 사라진다

- input은 parameter에 prompt message를 받을 수 있다.

  - sys.stdin.readline()은 받지않고 읽는 것만 가능하다.

    ```
    input('입력할 메세지 : ')
    ```

  - [지식in]('https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=381872141&qb=c3lzLnN0ZGluLnJlYWRsaW5lIGlucHV0&enc=utf8&section=kin.ext&rank=2&search_sort=0&spq=0')

##### * upper(), lower()

- upper()함수는 문자열의 모든 문자들을 대문자로 바꿔 줌
- lower()함수는 문자열의 모든 문자들을 소문자로 바꿔 줌
