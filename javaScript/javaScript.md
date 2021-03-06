## 브라우저(browser)

- 웹 서버에서 이동하며 클라이언트와 서버 간 양방향으로 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트 웨어
- 인터넷의 Content를 검색 및 열람하도록 함
- 주요 브라우저
  - Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safari



크로스 부라우징(Cross Browsing)

- W3C에서 채택된 표준 웹 기술을 채용하여 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되, 어느 한쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론(동일성이 아닌 동등성에 초점을 둠)
- 브라우저마다 렌더링에 사용하는 엔진이 다르기 때문



## JavaScript

- 브라우저 화면을 **동적**으로 만들어 준다

- 브라우저를 조작할 수 있는 유일한 언어

  - 

  ![image-20211027090658055](javaScript.assets/image-20211027090658055.png)



##### * 자바스크립트가  브라우저에서 할 수 있는 일

- DOM 조작 = 문서(HTML)조작

  - 문서(HTML)를 동적으로 만들 수 있다 (문서의 객체를 조작한다)

- BOM(Browser Object Model) 조작

  - 브라우저를 조작한다 (브라우저 각각의 객체를 조작한다)
  - navigator, screen, location, frames, history, XHR

- JavaScript Core(ECMAScript)

  - 자바스크립트의 문법 자체

  - 브라우저에서 할 수 있는 일 3가지

    - 프로그래밍 언어의 자바스크립트 일도 브라우저에서 진행할 수 있다

    1. Data Structure(Object, Array)를 만들 수 있다
    2. Conditional Expression(조건 표현식)
    3. Iteration(반복)



##### * Object Model

- 웹 브라우저의 구성요소들은 각각 객체화 되어있는 것을 말한다

- 자바스크립트는 이 각각의 객체들을 제어함으로써 웹 브라우저를 제어할 수 있다

- 객체들은 서로 계층적인 관계로 구조화 되어있다

  <img src="javaScript.assets/캡처1.JPG" alt="img" style="zoom: 80%;" />





##### * window 객체

- 자바스크립트의 최상위객체이자 전역객체이면서 모든 객체가 소속된 객체
- window는 객체화된 수 많은 구성 요소들로 이루어져 있다
  - 자바스크립트로 이 객체들을 제어해서 웹 브라우저를 제어할 수 있게 되는 것
  - 개발자도구에서 window를 치면 객체들을 확인할 수 있음



##### * DOM (데이터 구조)

- HTML, XML과 같은 문서에 접근하기 위한 문서 프로그래밍 인터페이스

- HTML 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델

  ![image-20211027095340733](javaScript.assets/image-20211027095340733.png)

- 문서과 구조화되어 있으며 각 요소는 객체(object)로 취급

  - 자바스크립트가 객체를 인식하여 조작을 할 수 있다

- 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능

- 주요 객체

  - window : DOM을 표현하는 창, 가장 최상위 객체(작성 시 생략 가능)
  - document : 페이지 컨텐츠의 Entry Point 역할을 하며, body와 같은 수많은 다른 요소들을 포함
  - navigator, location, history, screen

- 해석(파싱, Parsing)

  - 구문 분석, 해석
  - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

  ![image-20211027095626746](javaScript.assets/image-20211027095626746.png)

- 조작
  - JavaScript 언어로 조작하여 문서(HTML, web page)를 조작할 수 있다![image-20211027100443934](javaScript.assets/image-20211027100443934.png)



##### * BOM

- Browser Object Model

- 자바스크립트가 브라우저와 소통하기 위한 모델

  - window객체를 통해 접근이 가능하다

- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능

- window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭
  - document도 브라우저 내에 종속되어 있기 때문에 window 전역 객체에 포함된다

- ex) 
  - 탭 창 window.open(), 인쇄 창 window.print(), 메세지 및 대화상자 창 window confirm()

    | navigator | 브라우저 명과 버전정보를 속성으로 가짐                    |
    | --------- | --------------------------------------------------------- |
    | window    | 최상위 객체로, 각 프레임별로 하나씩 존재                  |
    | document  | 현재 문서에 대한 정보                                     |
    | location  | 현재 URL에 대한 정보 / 브라우저에서 사용자가 요청하는 URL |
    | history   | 현재의 브라우저가 접근했던 URL history                    |
    | screen    | 브라우저의 외부환경(운영체제 화면)에 대한 정보를 제공     |



##### * JavaScript Core(ECMAScript)

- 프로그래밍 언어로 사용

  ![image-20211027101314255](javaScript.assets/image-20211027101314255.png)

##### * DOM 조작

- Document는 문서 한 장(HTML)에 해당하고 이를 조작
  - 우리가 보는 웹 화면을 조작하는 것이라고 생각
  
- 조작 순서
  1. 선택(Select)
  2. 변경(Manipulation)

- document 위치
  
  ![image-20220109110042991](javaScript.assets/image-20220109110042991.png)

- 객체의 상속 구조

  - EventTarget
    - Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
      - ex) addEventListener가 가능한 객체
    
  - Node(틀에 대한 개념)
    - 여러 가지 DOM 타입들이 상속하는 인터페이스 

  - Element
    - Document 안의 모든 객체가 상속하는 가장 범용적인 기반 클래스
    - 부모인 Node와 그 부모인 EventTarget의 속성을 상속

  - Document
    - 브라우저가 불러온 웹 페이지를 나타냄
    - DOM 트리의 진입점(entry point) 역할을 수행
  - HTMLElement
    - 모든 종류의 HTML요소
    - 부모 element의 속성 상속 

  <img src="javaScript.assets/image-20211027102755073.png" alt="image-20211027102755073" style="zoom: 80%;" />

##### * DOM 선택

- 메서드

  - querySelector, querySelectorAll를 주의깊에 봐야하는 이유

    - id, class, tag 선택자 등을 모두 사용 가능하므로 더 구체적이고 유연하게 선택 가능

  - Document.querySelector(selector)

    - 인자에 CSS 선택자가 들어간다
    - 제공한 선택자와 일치하는 element 하나 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null)

  - Document.querySelectorAll(selector)

    - 제공한 선택자와 일치하는 여러 element를 선택

    - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    - 지정된 셀렉터에 일치하는 NodeLIst를 반환
      - 현재 문서에서 지정된 CSS selector에 일치하는 모든 태그들을 선택하면 List로 반환된다

  - getElementById(id)

  - getElementsByTagName(name)

  - getElementByClassName(names)

- 선택 메서드별 반환 타입

  1. 단일 element

     - querySelector(), getElementById()

  2. HTMLCollection

     - 배열과 같이 각 항목에 접근하기 위한 index를 제공(유사 배열)
     - name, id, index 속성으로 각 항목에 접근 가능

     - getElementsByTagName(), getElementByClassName()

  3. NodeList

     - 배열과 같이 각 항목에 접근하기 위한 index를 제공(유사 배열)
     - index로만 각 항목에 접근 가능
     - HTMLCollection과 달리 배열에서 사용하는 forEach함수 및 다양한 메서드 사용 가능

     - querySelectorAll()

  - HTMLCollection 와 NodeList 둘다 Live Collection으로 DOM의 변경사항을 실시간으로 반영
    - querySelectorAll()에 의해 반한되는 NodeList는 static Collection으로 실시간 반영X

- Collection
  1. Live Collection
     - 문서가 바뀔 때 실시간으로 업데이트 됨
     - DOM의 변경사항을 실시간으로 collection에 반영
     - HTMLCollection, NodeList
  2. Static Collection(non-live)
     - DOM이 변경되어도 collection 내용에는 영향을 주지 않음
     - querySelectAll()의 반환 NodeLIst만 Static collection



##### * DOM 변경

- 메서드(Creation)

  - Document.createElement()
    - 작성한 태그 명의 HTML 요소를 생성하여 반환
    - append()와 appendChild()를 이용하여 추가하기 위해서는 createElement()를 통해서 먼저 생성이 되어야 한다
  - Element.append() - Element를 객체라 생각
    - 특정 부모 Node의 자식 NodeList중 마지막 자식 다음에 **Node객체나 DOMString**을 삽입
    - **여러 개**의 Node객체, DOMString을 추가할 수 있음
    - 반환 값이 없음

  - Node.appendChild()
    - 한 Node를  특정 부모 Node의 자식 NodeList중 마지막 자식으로 삽입(**Node만 추가 가능**)
    - **한번에 오직 하나**의 Node만 추가할 수 있음
    - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
    - 추가된 Node 객체를 반환

- 메서드(proerty)

  - Node.innerText = '집어 넣을 값'

    - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (사람이 읽을 수 있는 내용만 남김)
      - 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현

  - Element.innerHTML

    - 요소(Element)내에 포함된 HTML 마크업을 반환

    - XSS 공격에 취약

    - [참고] XSS (Cross-site-Scripting)

      - 공격자가 웹 사이트 클아이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
      - 피해자의 브라우저가 악성 스크립트를 실행하며 공겨자가 엑세스 제어를 우회하고 사용자인 척 한다(CSRF공격과 유사)

      <img src="javaScript.assets/image-20211027114746038.png" alt="image-20211027114746038" style="zoom:80%;" />

- 메서드(삭제)
  - ChildNode.remove()
    - 자식 Node를 선택해서 제거
  - 부모Node.removeChild(자식Node)
    - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
    - Node는 인자로 들어가는 자식 Node의 부모 Node

- 메서드(속성)

  - Element.setAttribute(속성, 속성값)

    - 지정된 요소의 값을 설정

    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

  - Element.getAttribute(attributeName)
    - 해당 요소의 지정된 값(특정 속성값, 문자열)을 반환
    - 인자(attributeName)는 값을 얻고자 하는 속성의 이름

  - Element.removeAttribute(name)
    - Element의 속성 값을 지움

  - Element.hasAttribute(name)
    - Element의 속성 값이 있는지 없는지 True, Flase값 반환





##### * [Event](https://developer.mozilla.org/ko/docs/Web/Events) ( ~~하면 ~~ 한다)

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체

- 이벤트 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
    - ex) click, change, submit, load
  - 특정 메서드를 호출(Element.click())하여 프로그래밍적으로도 만들어 낼 수 있음
  
- Event기반 인터페이스
  - AnimationEvent, ClipboardEvent, DragEvent 등
  - UIEvent
    - 간단한 사용자 interface event
    - Event의 상속을 받음
    - MouseEvent, KeyboardEvent, InputEvent, FocusEvent 등의 부모 객체 역할을 함

- Event handler (Event를 처리)

  - 대상에 특정 이벤트가 발생하면, 할 일을 등록하자

  - EventTarget.addEventListener(type, listener[, options])

    - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 인자에 설정
    - 이벤트를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능
    - type
      - 반응 할 이벤트 유형(대소문자 구분 문자열)
    - listener
      - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
      - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함
      - event 값이 인자로 자동으로 넘어온다
    
  - ex) 클릭하면 알림창을 띄우는 addEventListener

    ```html
    # 방법1
    <body>
        <button type="button">버튼</button>
        
        <script>
        	const btn = document.querySelector("button")
            btn.addEventListener("click", function (event)){
              alert("버튼이 클릭되었습니다.")
              console.log(event)
            })
        </script>
    </body>
    # 방법2
    <body>
        <button onlick="alertMessage()">버튼</button>
        
        <script>
            const alertMessage = function () {
                alert("버튼이 클릭되었습니다.")
            }
        </script>
    </body>

- Event 취소

  - Event.preventDefault()
  
  - 현재 이벤트의 기본 동작을 중단
  
  - 태그의 기본 동작을 작동하지 않게 막음
    - ex) a태그의 기본 동작은 클릭 시 링크로 이동/ form 태그의 기본 동작은 form 데이터 전송
    
  - 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소
  
  - 취소 할 수 없는 이벤트도 존재
  
    - 이벤트의 취소 가능 여부는 event의 data값에 cancelable을 통해 확인이 가능하다
  
      -  event.cancelable을 사용해 확인할 수 있음(false면 취소 불가능)
    
        ![image-20220109193700899](javaScript.assets/image-20220109193700899.png)
    
    - ex) 대표적인 취소할 수 없는 이벤트 : 스크롤 이벤트



##### * CREATE, READ 기능을 충족하는 todo app만들어보기

```html
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE-edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="#">
        <input type="text">
        <button>Add</button>
    </form>
    <ul>
        
    </ul>
    <script>
        // 이벤트 타켓 설정
        const form = document.querySelector("form")
        
        form.addEventListener("submit", function (event) {
          event.preventDefault() // event의 기본동작을 막는다
            
          // 1. input 선택 및 value 값 선택
          const input = document.querySelector("input")
          const content = input.value
          
          if (content.trim()) {
            // 새로운 li 요소 생성, input value를 innerText로 넣는다
            const liTag = document.createElement("li")
            liTag.innerText = content
        	
            // ul 요소를 선택, ul의 자식 요소로 li요소를 추가한다
            const ulTag = document.querySelector("ul")
            ulTag.appendChild(liTag)
          } else {
            alert('할 일을 입력해주세요!')
          }
          
          // event 타겟을 reset(input창에 입력된 값 초기화)
          event.target.reset()
        })
    </script>
</body>
</html>
```





## AJAX

- Asynchronous JavaScript And XML (비동기식 JavaScript와 XML)
- 서버와 통신하기 위해 XMLHttpRequest 객체를 활용
- JSON, XML, HTML 그리고 일반 텍스트 형식 등을 퐇마한 다양한 포맷을 주고 받을 수 있음
  - AJAX의 X가 XML을 의미하긴 하지만, 요즘은 더 가벼운 용량과 JavaScript의 일부라는 장점 때문에 JSON을 더 많이 사용함

- 특징
  - 페이지 전체를 reload(새로고침)를 하지 않고서도 수행되는 비동기성
    - 사용자의 event가 있으면 전체 페이지가 아닌 일부분만을 업데이트 할 수 있음
  - AJAX의 주요 두가지 특징
    1. 페이지 새로고침 없이 서버에 요청
    2. 서버로부터 데이터를 받고 작업을 수행

- Google 사용 예시
  - Gmail
    - 메일 전송 요청이 모두 처리 되기 전 다른 페이지로 넘어가더라도 메일은 전송 됨
  - Google Maps
    - 스크롤 행위 하나하나가 모두 요청이지만 페이지는 갱신X

- XMLHttpRequest 객체
  - 서버와 상호작용하기 위해 사용되며 전체 페이지의 새로고침 없이 데이터를 받아올 수 있음
  - 사용자의 작업을 방해하지 않으면서 페이지 일부를 업데이트할 수 있음
  - 주로 AJAX 프로그래밍에 사용
  - 이름과 달리 XML 뿐만 아니라 모든 종류의 데이터를 받아올 수 있음
  - 생성자
    - XMLHttpRequest()

- XMLHttpRequest 예시

  - console에 todo 데이터가 출력X

    - 데이터 응답을 기다리지 않고 console.log()를 먼저 실행했기 때문이다.

    ```javascript
    const request = new XMLHttpRequest()
    const URL = 'https://jsonplaceholder.typicode.com/todos/1/'
    
    request.open('GET', URL)
    request.send() // 요청
    
    const todo = request.response // 응답 데이터 저장
    console.log(`data: ${todo}`) // 출력



##### * 동기식

- 순차적, 직렬적 Task 수행
- 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐(blcoking)

- ex)

  - 버튼 클릭 후 alert 메시지의 확인 버튼을 누를 때까지 문장이 만들어지지 않음

  - 즉, alert 이후의 코드는 alert의 처리가 끝날 때까지 실행되지 않음

  - 왜 이런 현상 -> JavaScript는 single threaded

    <img src="javaScript.assets/image-20220110043104152.png" alt="image-20220110043104152" style="zoom: 80%;" />



##### * 비동기식

- 병렬적인 듯한 Task 수행
  - JavaScript는 single threaded
- 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐(non-blocking)

- ex)

  - 요청을 보내고 응답을 기다리지 않고 다음 코드가 실행됨

  - 결과적으로 변수 todo에는 응답 데이터가 할당되지 않고 빈 문자열이 출력

  - 그렇다면 JS는 왜 기다려주지 않는 방식으로 동작하는가?

    - JavaScript는 single threaded

    <img src="javaScript.assets/image-20220110043337828.png" alt="image-20220110043337828" style="zoom: 67%;" />

- 사용 이유
  - 사용자 경험 때문
  - 매우 큰 데이터를 동반하는 앱이 있다고 가정할 때 동기식 코드라면 데이터를 모두 불러온 뒤 앱이 실행됨
    - 데이터를 모두 불러올 때 까지는 앱이 모두 멈춘 것처럼 보임
    - 코드 실행을 차단하여 화면이 멈추고 응답하지 않는 것 같은 사용자 경험을 제공
  - 비동기식 코드라면 데이터를 요청하고 응답 받는 동안, 앱 실행을 함께 진행함
    - 데이터를 불러오는 동안 지속적으로 응답하는 화면을 보여줌으로써 더욱 쾌적한 사용자 경험을 제공
  - 웹 API 기능은 현재 비동기 코드를 사용하여 실행됨



##### * Threads

- 프로그램이 작업을 완료하기 위해 사용할 수 있는 단일 프로세스(일처리를 할 수 있는 머리)
- 각 스레드는 한 번에 하나의 작업만 수행할 수 있음
- ex) Task A -> TaskB -> Task C
  - 다음 작업을 시작하려면 반드시 앞의 작업이 완료되어야 함
  - 컴퓨터 CPU는 여러코어를 가지고 있기 때문에 한번에 여러 가지 일을 처리가능



##### - Blocking vs Non-Blocking

1. 요청

<img src="javaScript.assets/image-20220110044316092.png" alt="image-20220110044316092" style="zoom:67%;" />

2. 응답을 기다림

   - 응답을 기다리는 동안 python은 제자리, js는 할당하는 곳으로 넘어감 (현재응답 받지못함)

     ![image-20220110044453483](javaScript.assets/image-20220110044453483.png)

3. 응답을 받음

   - 파이썬은 응답을 받아 저장, js는 응답을 받은상태에서 이미 할당부분을 넘어 출력되는 부분

     ![image-20220110044602706](javaScript.assets/image-20220110044602706.png)

4. 최종

   - 결과적으로 변수 todo에는 응답 데이터가 할당되지 않고 빈 문자열이 출력

   <img src="javaScript.assets/image-20220110044636134.png" alt="image-20220110044636134" style="zoom:67%;" />

- JavaScript는 Sing threaded
- 컴퓨터가 여러 개의 CPUT를 가지고 있어도 main thread라 불리는 단일 스레드에서만 작업 수행
- 이벤트를 처리하는 Call stack이 하나인 언어라는 의미
- 문제해결
  1. 즉시 처리하지 못하는 이벤트들을 다른 곳(Web API)으로 보내서 처리하도록 한다
  2. 처리된 이벤트들은 처리된 순서대로 대기실(Task queue)에 줄을 세워 놓는다
  3. Call stack이 비면 담당장(Event Loop)가 대기 줄에서 가장 오래된 (제일 앞의)이벤트를 Call stack으로 보낸다



##### * JavaScript 동작원리

- 자바스크립트는 싱글 쓰레드 기반 언어

  - 호출 스택이 하나 = 한 번에 한 작업만 처리 가능
  - 호출 스택 : 프로그램 상에서 어디에 있는지를 기록하는 자료구조
  - 호출 스택이 최대 허용치를 넘으면 브라우저에서 에러발생

- setTimeout, EventListener, Ajax 같이 처리가 오래걸리는 코드는 동작순서가 뒤로 밀리고 빠르게 처리가능한 코드부터 처리한 뒤 처리된다.

  - 코드

    ```javascript
    function multiply(x, y) {
        return x * y;
    }
    function printSquare(x) {
        var s = multiply(x, x);
        console.log(s);
    }
    printSquare(5);
    ```

  - 실행 결과

    <img src="javaScript.assets/image-20220110025944475.png" alt="image-20220110025944475" style="zoom:50%;" />

- 반복문 코드를 짤 때 반복이 깊게 일어나면 js로는 구현하지 않는게 좋다.

  - ex) 30초가 걸리는 어려운 연산이 있을 때 eventListener는 30초 뒤에 실행된다.
    - 어려운 연산이 해결될 때까지 브라우저는 기능이 정지된다.
  - 비동기 콜백이 필요



##### * 호출 스택

- 함수의 호출, 자료구조의 스택
- 자바스크립트는 위쪽에서 아래로, 왼쪽에서 오른쪽으로 실행된다
- 자바스크립트가 동기적 코드로 실행될 때 순서를 파악하기 위함
  - 비동기적 코드는 호출스택만으로 설명이 불가능하다
- Anonymous은 가상의 전역 Context(항상 있다고 생각하는게 좋다)
  - 기본적으로 파일이 실행될 때, Anonymous가 처음에 쌓인다
- 함수 호출 순서대로 쌓이고, 역순으로 실행 됨
  - 밑에서부터 쌓이고 위에서부터 빠져나간다
- 함수 실행이 완료되면 스택에서 빠진다
- LIFO(Last In First Out)구조라서 스택이라고 불린다



##### * Concurrency model

- Event loop를 기반으로 하는 동시성 모델

1. Call stack(호출 스택)
   - 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO)형태의 자료 구조
2. WebAPI(Browser API) - 백그라운드?
   - JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
     - js는 한번에 하나(스택에서 한개의 일)만 수행 Stack에서 처리할 수 없는 일에 대해서는 Web API로 보낸다
   - setTimeout(), DOM events, AJAX로 데이터를 가져오는 시간이 소요되는 일들을 처리
     - setTimeout()의 설정시간은 출력을 보장하는 것이 아니라, TaskQueue로 넘어가는데 시간
     - setTimeout이 0초여도 무조건 WebAPI로 넘어온다
   - WebAPI(백그라운드)에서는 누가 먼저 실행될 지 모른다
     - 먼저 끝난 쪽이 TaskQueue로 넘어간다
3. TaskQueue(Event Queue, Message Queue)
   - 비동기 처리된 callback 함수가 대기하는 Queue(FIFO)형태의 자료 구조
     - WebAPI에서 처리되는 event들이 바로 Call Stack으로 Push되지않고 TaskQueue에서 대기
   - Call Stack이 비어있을 때 TaskQueue에서 넘어갈 수 있다
   - main  thread가 끝난 후 실행되어 후속 JavaScript코드가 차단 되는 것을 방지
   - Promise가 SetTimeout보다 우선순위가 높다
     - SetTimeout이 먼저 TaskQueue로 넘어와도 뒤늦게 넘어온 Promise가 먼저 실행
   - Process의 nextTick가 SetTimeout보다 우선순위가 높다
4. Event Loop
   - Call Stack이 비어있는지 확인
   - 비어 있는 경우 Task Queue에서 실행 되기 중인 callback함수가 있는지 확인
   - Task Queue에 대기 중인 callback 함수가 있다면 가장 앞에 있는 callback 함수를 Call stack으로 push

- ex)예시코드

  ```javascript
  console.log('Hi')
  
  setTimeout(function ssafy() {
    console.log('SSAFY')
  }, 3000)
  
  console.log('Bye')

- 동작원리

  1. Call Stack으로 들어가고 출력된 뒤 빠진다

     <img src="C:\Users\Administrator\Desktop\TIL\javaScript\javaScript.assets\image-20220114152752700.png" alt="image-20220114152752700" style="zoom: 50%;" />

  2. setTimeout이 Call Stack에 들어갔다가 ssafy 함수를 바로 실행할 수 없으므로 WebAPI로 보낸다.

     ![image-20220114153124907](C:\Users\Administrator\Desktop\TIL\javaScript\javaScript.assets\image-20220114153124907.png)

  3. Call Stack으로 들어가고 출력된 뒤 빠진다

     <img src="C:\Users\Administrator\Desktop\TIL\javaScript\javaScript.assets\image-20220114153330419.png" alt="image-20220114153330419" style="zoom:50%;" />

  4. 3초가 지나면 WebAPI에 있던 ssafy콜백함수가 Task Queue로 이동

     ![image-20220114153514644](C:\Users\Administrator\Desktop\TIL\javaScript\javaScript.assets\image-20220114153514644.png)

  5. ssafy 콜백함수가 Call Stack으로 이동한 뒤 호출되고 빠진다.

     <img src="C:\Users\Administrator\Desktop\TIL\javaScript\javaScript.assets\image-20220114153727703.png" alt="image-20220114153727703" style="zoom:50%;" />



##### * Zero delays

- 실제로 0ms 후에  callback함수가 시작된다는 의미가 아님
- 실행은 Task Queue에 대기 중인 작업 수에 따라 다르며 해당 예시에서는 callback 함수의 메시지가 처리되기 전에 'HI', 'Buy'가 먼저 출력됨
  - delay(지연)는 JavaScript가 요청을 처리하는데 필요한 최소 시간이다(보장된 시간이 아님)
- setTimeout 함수에 특정 시간제한을 설정했더라도 대기 중인 메시지의 모든 코드가 완료될 때까지 대기해야 한다.



##### * 순차적인 비동기 처리하기

- Web API로 들어오는 순서는 중요하지 않고, 어떤 이벤트가 먼저 처리되느냐가 중요
  - 실행 순서 불명확
- 실행 순서 불명확 현상을 해결하기 위해 순차적인 비동기 처리를 위한 2가지 작성 방식
  1. Async callbacks(비동기 콜백)
     - 백그라운드에서 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
     - ex) addEventListener()의 두번째 인자 : 콜백함수
  2. promise-style
     - Modern Web APIs에서의 새로운 코드 스타일
     - XMLHttpRequest 객체를 사용하는 구조보다 조금 더 현대적인 버전





##### * Callback Function

- 다른 함수에 인자로 전달된 함수
- 외부 함수 내에서 호출되어 루틴 또는 작업을 완료함

- 동기식, 비동기식 모두 사용됨
  - 비동기 작업이 완료된 후 코드 실행을 계속하는 데 주로 사용
- 비동기 작업이 완료된 후 코드 실행을 계속하는 데 사용되는 경우 : 비동기 콜백(Async callbacks)

- JavaScript의 함수는 일급객체(일급함수)

  - 다른 객체들에 적용할 수 있는 연산을 모두 지원하는 객체(함수)

  - 일급 객체의 조건

    1. 인자로 넘길 수 있어야 한다
    2. 함수의 반환 값으로 사용할 수 있어야 한다
    3. 변수에 할당할 수 있어야 한다

  - Callback Function 예시

    ```javascript
    // 
    const myFunc = function (func) {
        return func
    }
    
    const myArgumentFunc = function () {
        return 'Hello'
    }
    
    const result = myFunc(myArgumentFunc)
    console.log(result)
    /* 출력
    f () {
        return 'Hello'
    }
    */
    
    // map
    const nums = [1, 2, 3]
    const doubleNums = nums.map(num => {
        return num * 2
    })
    console.log(doubleNums) // 출력 : [2, 4, 6]
    
    // Array Helper Method (array 메서드)
    const numbers = [1, 2, 3]
    const newNumbers = []
    
    numbers.forEach(num => {
        newNumbers.push(num + 1)
    })
    console.log(newNumbers) // [2, 3, 4]
    
    // setTimeout
    const helloworld = function () {
        console.log('happy coding!!')
    }
    setTimeout(helloworld, 3000)
    console.log('unhappy coding!!')
    /* unhappy coding!! 먼저 출력 후 WebAPI에서 3초간 돌고 que -> callstack -> 출력 */
    
    //addEventListener
    <body>
      <button>버튼</button>
    
      <script>
        const myButton = document.querySelector('button')
    	myButton.addEventListener('click', function() { // 두번째 인자가 콜백함수
            console.log('button clicked!!')
        })
      </script>
    </body>
    ```

    <img src="C:\Users\Administrator\Desktop\TIL\javaScript\javaScript.assets\image-20220114194600254.png" alt="image-20220114194600254" style="zoom:80%;" />



##### * Async callbacks

- 백그라운드에서 코드 실행을 시작할 함수를 호출할 때 인자로 지정된 함수

- 백그라운드 코드 실행이 끝나면 callback 함수를 호출하여 작업이 완료되었음을 알리거나, 다음 작업을 실행하게 할 수 있음

  - ex) adEventListener()의 두번째 매개변수

- callback 함수를 다른 함수의 인자로 전달할 때, 함수의 참조를 인자로 전달할 뿐이지 즉시 실행되지 않고, 함수의 body에서 called back됨.

  - 정의된 함수는 때가 되면 callback 함수를 실행하는 역할을 함
  - addEventListener()에서 콜백함수는 바로 실행되지 않는다

- Why use callback?

  - 콜백 함수는 명시적인 호출이 아닌 특정 루틴 혹은 action에 의해 호출되는 함수
  - Django의 "요청이 들어오면", event의 경우 "특정 이벤트가 발생하면"이라는 조건으로 함수를 호출 할 수 있었던 건 "Callback function"개념 때문에 가능하다

  - 비동기 로직을 수행할 때 callback 함수는 필수
    - 명시적인 호출이 아니라 다른 함수의 매개변수로 전달하여 해당 함수 내에서 특정 시점에 호출



##### * callback Hell(콜백지옥)

- 순차적인 연쇄 비동기 작업을 처리하기 위해 "callback 함수를 호출하고, 그 다음 callback 함수를 호출하고, 또 그 함수의 callback 함수를 호출하고.."의 패턴이 지속적으로 반복됨

  - 여러 개의 연쇄 비동기 작업을 할 때 마주하는 상황

  - pyramid of doom(파멸의 피라미드)라고도 한다

- 콜백지옥이 일어나면 디버깅, 코드 가독성이 어려워진다

  <img src="javaScript.assets/image-20220114225441578.png" alt="image-20220114225441578" style="zoom: 67%;" />

- 해결
  1. Keep your code shallow (코드의 깊이를 얕게 유지)
  2. Modularize (모듈화)
  3. Handle every single error (모든 단일 오류 처리)
  4. Promise callbacks (Promise 콜백 방식 사용)



##### * [Axios](https://axios-http.com/kr/docs/intro)

- Promise based HTTP client for the browser and Node.js
  - 응답을 Promise 객체로 준다
  - Promise 객체에는 config, data, headers, request, status, statusText 등 값들이 존재
  
- 브라우저를 위한 Promise 기반의 클라이언트

- Priomise 내부까지는 동기, then & catch를 만나는 순간 비동기

- 원래는 "XHR"이라는 브라우저 내장 객체를 활용해 AJAX 요청을 처리하는데, 이보다 편리한 AJAX 요청이 가능하도록 도움을 준다
  - 확장 가능한 인터페이스와 함께 패키지로 사용이 간편한 라이브러리를 제공

- [Axios를 사용하기 위해서는 설치 혹은 CDN으로 불러오기 작업 필요](https://github.com/axios/axios)

  ```css
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

- XMLHttpRequest -> Axios 변경

  - XMLHttpRequest를 사용했을 때 todo에 요청에 따른 응답의 값이 들어있지 않았었다
  - Axios의 .then()을 사용하면 성공을 했을 때 콜백함수가 실행되므로 data가 제대로 넘어온다
    - 값의 누락X

  <img src="javaScript.assets/image-20220114234729030.png" alt="image-20220114234729030" style="zoom:50%;" />

- ex)

  <img src="javaScript.assets/image-20220115000112628.png" alt="image-20220115000112628" style="zoom: 67%;" />

- instance method

  ```
  axios.get(url[, config])
  axios.post(url[, data[, config]])
  axios.put(url[, data[, config]])
  axios.patch(url[, data[, config]])
  axios.delete(url[, config])
  axios.request(config)
  axios.head(url[, config])
  axios.options(url[, config])
  axios.getUri([config])

- configs (구성)

  - url : 요청에 사용될 서버 URL

    ```javascript
    axios({
      url: 'http://localhost:5000',
    });

  - method : 요청에 사용될 메소드(GET, POST, PUT, PATCH, DELELTE)

    - GET : 리소스(HTTP 요청의 대상) 조회
    - POST : 요청 데이터 처리
    - PUT : 리소스를 대체, 해당 리소스가 없으면 생성
    - PATCH : 리소스를 일부만 변경
    - DELELTE : 리소스 삭제

    ```javascript
    axios({
      method: 'get', /* get, post, put patch, delete */
    });

  - baseURL : url 값이 절대경로 url이 아니라면, 앞 부분에 baseURL값이 붙는다

    ```javascript
    axios({
      url: '/users',
      baseURL: 'http://localhost:5000/',
    });

  - transformRequest : 서버에 요청을 보내기 전에 데이터를 변환

    ``` javascript
    axios({
      data: { id: 1 },
      transformRequest: [function(data, headers) {
        const payload = { ...data, key: 'some-key' };
        return qs.stringify(payload);
      }],
    });
    ```

  - transformResponse : 서버에서 받은 데이터를 변경해서 then/catch로 전달

    ```javascript
    axios({
      transformResponse: [function(data) {
        const tmpData = JSON.parse(data);
        return tmpData.data.map((item, i) => {
          item.index = 1;
          return item;
        });
      }],
    }).then(result => {
      console.info(result.data); // [ { id: 1, index: 0 }, { id: 2, index: 1 } ]
    });
    ```

  - headers : 서버에 전송될 사용자 정의 헤더

  - params : 요청 URL과 같이 전송될 매개변수

    ```javascript
     /* http://localhos:5000?key=3 이렇게 요청을 보낸 것과 동일하다 */
    axios({
      url: 'http://localhost:5000/',
      params: { key: 3 },
    });
    ```

  - paramsSerializer : params를 직렬화하는 옵션 함수

    ```javascript
    /* params에 배열을 전송할 시, 요청을 받는 서버 쪽에서는 { 'key[]:[ '1', '2', '3' ] }
    의 형태로 받는다. 하지만 직렬화로 인해 { key: '1,2,3' } 의 형태로 받는다. */
    axios({
      params: { key: [1, 2, 3] },
      paramsSerializer: paramObj => {
        const params = new URLSearchParams();
        for (const key in paramObj) {
            params.append(key, paramObj[key])
        }
        return params.toString();
      },
    });
    ```

  - data : request body로 전송할 데이터 (put, post, patch에만 적용 가능)

    ```javascript
    axios({
      data: { id: 3 },
    });
    ```

  - timeout : 요청이 타임아웃되는 ms를 지정 (기본값 : 0)

    - 요청이 해당 설정 시간보다 지연될 경우 요청 중단, catch로 에러 전달

    ```javascript
    axios({
      timeout: 1000,
    });
    ```

  - withCredentials : 자격 증명을 사용하여 크로스 사이트 접근 제어 요청이 필요한 경우 설정

    - 서버와 클라이언트 도메인이 서로 다르면 쿠키 전송이 되지 않을 때 사용

    ```javascript
    const httpAdapter = require('axios/lib/adapters/http');
    const settle = require('axios/lib/core/settle');
    
    axios({
      url: 'http://localhost:5000/',
      adapter: config => {
        return new Promise((resolve, reject) => {
          httpAdapter(config).then(response => {
            if (response.status === 200) {
              response.status = 503;
            }
            settle(resolve, reject, response);
          }).catch(reject);
        });
      },
    }).catch(err => {
      console.error(err); // Error: Request failed with status code 503 ...
    });
    ```

  - adapter : 커스텀 핸들링 요청을 허용, 유효한 응답(Promise)를 반환

    ```javascript
    /* response status 가 200 일 경우 503 으로 세팅해 응답하도록 adapter 를 추가 
    정상적으로 왔을 응답이 503 에러로 처리되어 catch 에서 찍힌다*/
    const httpAdapter = require('axios/lib/adapters/http');
    const settle = require('axios/lib/core/settle');
    
    axios({
      url: 'http://localhost:5000/',
      adapter: config => {
        return new Promise((resolve, reject) => {
          httpAdapter(config).then(response => {
            if (response.status === 200) {
              response.status = 503;
            }
            settle(resolve, reject, response);
          }).catch(reject);
        });
      },
    }).catch(err => {
      console.error(err); // Error: Request failed with status code 503 ...

  - auth : HTTP 기본 인증이 사용되며 자격 증명을 제공함을 나타낸다

    - 기존의 Authorization 헤더를 덮어쓰는 헤더 설정이 들어가게 된다.

    ```javascript
    axios({
      auth: {
        username: 'dongil',
        password: 'test',
      },
    });
    ```

  - responseType : 서버에서 응답할 데이터 타입을 설정

    - [ 'arraybuffer', 'blob', 'document', 'json', 'text', 'stream' ]

    ```javascript
    axios({
      responseType: 'json'
    });
    ```

  - responseEncoding : 응답 디코딩에 사용할 인코딩을 나타낸다

    - 클라이언트 사이드 요청 또는 responseType이 stream인 경우 무시

    ```javascript
    axios({
      responseEncoding: 'utf8' // 기본값
    });
    ```

  - xsrfCookieName : xsrf 토큰(token)에 대한 값으로 사용할 쿠키 이름

    ```javascript
    axios({
       xsrfCookieName: 'XSRF-TOKEN', // 기본 값
    });
    ```

  - xsrfHeaderName : xsrf 토큰값을 운반하는 HTTP 헤더 이름

    ```javascript
    axios({
      xsrfHeaderName: 'X-XSRF-TOKEN', // 기본 값
    });
    ```

  - onUploadProgress : 업로드 프로그레스 이벤트를 처리

    ```javascript
    axios({
      onUploadProgress: progressEvent => {
        ...
      },
    
    });
    ```

  - onDownloadProgress : 다운로드 프로그레스 이벤트를 처리

    ```javascript
    axios({
      onDownloadProgress: progressEvent => {
        ...
      },
    });
    ```

  - maxContentLength : HTTP 응답 콘텐츠의 최대 크기를 바이트(Bytes) 단위로 설정

    ```javascript
    axios({
      maxContentLength: 2000,
    });
    ```

  - vaildateStatus : 응답 상태 코드에 대해  true or false로 promise를 resolve하거나 reject

    ```javascript
    /* 응답코드 200 외에는 전부 에러로 처리 */
    axios({
      validateStatus: status => {
        // return status >= 200 && status < 300; - default
        return status !== 200;
      },
    });
    ```

  - maxRedirect : Node.js에서 리다이렉션이 가능한 최대 갯수를 정의

    ```javascript
    axios({
      maxRedirect: 5,
    });
    ```

  - cancelToken : 요청을 취소

    ```javascript
    /* cancelToken 을 넣어 보내면, 요청이 취소되어 reject 로 처리되고 그 에러가 cancel 된 요청인지도 확인가능 */
    const axios = require('axios');
    const CancelToken = axios.CancelToken;
    const source = CancelToken.source();
    
    axios({
      url: 'http://localhost:5000/',
      cancelToken: source.token,
    }).catch(err => {
      console.error(err); // Cancel { message: 'Want to cancel' }
      console.info(axios.isCancel(err)); // true
    });
    
    source.cancel('Want to cancel');
    ```

- 응답 스키마

  - 요청에 따른 응답 결과는 아래의 정보들이 들어 있다

    - data : 서버가 제공한 응답 데이터
    - status : 서버 응답의 HTTP 상태 코드
    - statusText : 서버 응답으로 부터의 HTTP 상태 메시지
    - headers : 서버가 응답 한 헤더는 모든 헤더 이름이 소문자로 제공
    - config : 요첨에 대해 axios에 설정된 구성 confing
    - request : 응답을 생성한 요청

    ```javascript
    {
      data: {},
      status: 200,
      statusText: 'OK',
      headers: {},
      config: {},
      request: {}
    }
    
    /* then을 사용하면 응답을 받을 수 있다 */
    axios.get('/user/12345')
      .then(function (response) {
        console.log(response.data);
        console.log(response.status);
        console.log(response.statusText);
        console.log(response.headers);
        console.log(response.config);
      });



##### * Promise

- 내용이 실행은 되었지만 결과를 아직 반환하지 않은 객체

- axios.get(URL)에 대한 응답의 결과도 Promise객체

  ```javascript
  const myPromise = axios.get(URL)
  console.log(myPromise) // 출력 : Promise Object

-  비동기 작업의 최종 완료 또는 실패를 나타내는 객체

  - 미래의 결과(완료 또는 실패) 값을 타나냄
  - 미래의 어떤 상황에 대한 약속

- 연쇄작업에 대해서 구조를 나눠 순차적으로 모듈화

  - 순서보장, 가독성 증가

- .then()과 .error()의 콜백함수가 무조건 다음 .then()이나 .catch()로 넘어가려면 return이 존재해야 한다

- .then(callback함수)

  - 성공(이행)에 대한 약속

  - 이전 작업(promise)이 성공했을 때(이행했을 때) 수행할 작업을 나타내는 callback 함수

  - 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받는다.

    ```javascript
    const myPromise = axios.get(URL)
    
    axios.get(URL)
      .then(response => { // response는 myPromise(axios.get(URL))의 결과
        return response.data // 결과
    })
    // 위의 .then()이 성공적으로 이행된다면 다음 .then()이 실행
    // 다음 then()으로 오기 위해서 이전에 콜백함수가 return이 있어야 한다.
      .then(response => { // response는 바로 위의 .then()의 결과인 response.data
        return response.title
    })

  - 성공했을 때의 코드를 callback 함수 안에 작성

- .catch(callback함수)

  - 실패(거절)에 대한 약속

  - .then이 하나라도 실패하면(거부 되면) 동작 (동기식의 'try-except'구문과 유사)

  - axios에 요청을 보내는 주소가 잘못되었을 때도 .catch()가 실행된다

  - 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있음

    ```javascript
    const myPromise = axios.get(URL)
    
    axios.get(URL)
      .catch(error => { // error는 myPromise(axios.get(URL))의 결과가 인자로 들어온다
        console.log(error)
    })

- .finally(callback함수)

  - Promise 객체를 반환
  - 결과와 상관없이 무조건 지정된 callback 함수가 실행
  - 어떠한 인자도 전달받지 않는다
    - Promise가 성공되었는지 거절되었는지 판단할 수가 없기 때문
  - 무조건 실행되어야 하는 절에서 활용
    - .then()과 .catch() 블록에서의 코드 중복을 방지

- `Promise.all(배열)` : 여러 개의 Promise를 동시에 실행

  - 하나라도 실패하면 catch로 넘어감
  - allSettled로 실패한 것만 추려낼 수 있다

  ```javascript
  [ㅐ]const promise1  = Promise.resolve("성공1");
  const promise2  = Promise.resolve("성공2");
  Promise.all([promise1, promise2])
    .then((result) => {
      console.log(result); // ['성공1', '성공2'];
    }
    .catch((error) => {
      console.log(error);
    });
  ```

- `.resolve(value)` : 주어진 값으로 이행하는 Promise.then 객체를 반환

  - `value`가 Promise에 의해 결정되는 인수

- `.reject(reason)` : 주어진 이유(reason)로 거부된 Promise 객체를 반환

  - `reason`이 Promise를 거부한 이유

  ```javascript
  const condition = true; // true면 resolve, false면 reject
  const promise = new Promise((resolve, reject) => {
    if (condition) {
      resolve("성공");
    } else {
      reject("실패");
    }
  });
  
  promise
    .then((message) => {
      console.log(message); // 성공
    })
    .catch((error) => {
      console.log(error); // 실패
    })

- then() & catch()

  - .then() 블록은 서로 다른 promise를 반환

    - .then() 세트 1개당 promise를 반환한다

  - .then()과 .catch() 메서드는 모두 promise를 반환하기 때문에 **chaining** 가능

    - 반환 값이 반드시 있어야함
      - 다음 콜백함수에서 반환 값을 인자로 사용
    - 반환 값이 없다면 callback 함수가 이전의 promise 결과를 받을 수 없음

    ```javascript
    const myPromise = axios.get(URL)
    
    //chaining
    axios.get(URL)
      .then(response => { // response는 myPromise(axios.get(URL))의 결과
        return response.data // 결과
    })
    // 위의 .then()이 성공적으로 이행된다면 다음 .then()이 실행
    // 다음 then()으로 오기 위해서 이전에 콜백함수가 return이 있어야 한다.
      .then(response => { // response는 바로 위의 .then()의 결과인 response.data
        return response.title
    })
      .catch(error => { // error는 위의 .then() 결과가 인자로 들어온다
        console.log(error)
    })
      .finally(function () {
        console.log('나는 마지막에 무조건 실행!!')
    })

- callback Hell를 Promise로 바꿔보기

  - callback Hell

    ```javascript
    work1(function(resul1) {
      work2(result1, function(result2) {
        work3(result2, function(result3) {
          console.log('최종 결과: ' + result3)
        })
      })
    })

  - Promise

    ```javascript
    work1().then(function(result1) {
        return work2(result1)
    })
    .then(function(result2) {
        return work3(result2)
    })
    .then(function(result3) {
        console.log('최종결과: ' + result3)
    })
    .catch(failureCallback)

- Promise가 Async callback 작성 스타일과 달리 Promise가 보장하는 특징
  1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
     - Promise callback함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
  2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
  3. .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음(Chaining)
     - 각각의 callback은 주어진 순서대로 하나하나 실행하게 된다
     - Chaining은 Promise의 가장 뛰어난 장점

- ex)

  ```html
  <script>
    const URL = 'https://dog.ceo/api/breeds/image/random'
    const myButton = document.querySelector('button')
    
    //버튼을 클릭하면, dog api로 요청을 보냄
    myButton.addEventListener('click', function() {
        axios.get(URL)
          .then(response => {
            return response.data
          })
          .then(response => {
            const imgUrl = response.message
            // img 태그 생성
            const newImgTag = document.createElement('img')
            // img 태그의 src 속성에 imgUrl 값 할당
            newImgTag.src = imgUrl
            // div 태그의 자식 태그로 완성된 img 태그를 삽입
            const dogBox = document.querySelector('.dog-box')
            dogBox.appendChild(newImgTag)
          })
          .catch(error => {
            console.log(error)
          })
    })
  </script>





##### * async & await

- ES8에 등장한 비동기 코드를 작성하는 새로운 방법

- 기존 Promise 시스템 위에 구축된 syntactic sugar
  - promise 구조의 then chaining을 제거
  - 비동기 코드를 조금 더 동기 코드처럼 표현
  - Syntactic sugar
    - 더 쉽게 읽고 표현할 수 있도록 설계된 프로그래밍 언어 내의 구문
    - 문법적 기능은 그대로 유지, 사용자가 직관적으로 코드를 읽을 수 있게 만듦

- async & await 사용방법

  1. 함수의 앞에 async라는 예약어를 붙인다
  2. 함수의 내부 로직 중 HTTP 통신을 하는 비동기 처리 코드 앞에 await을 붙인다
     - 비동기 처리 메서드가 꼭 Promise 객체를 반환해야 await가 의도한대로 동작
     - await의 대상이 되는 비동기 처리 코드는Axios 등 promise를 반환하는API 호출 함수
  3. 예외 처리
     - .then() -> try{}
     - .catch() -> catch{}

  - ex)

    ```
    async function 함수명() {
      await 비동기 처리 메서드명();
    }

- Promise -> async & await로 변환

  - promise

    <img src="javaScript.assets/image-20220115000733075.png" alt="image-20220115000733075" style="zoom:80%;" />

  - async & await

    - fetchDogImage함수가 서버에서 사용자 정보를 가져오는 HTTP 통신코드라 가정

    <img src="javaScript.assets/image-20220115000754508.png" alt="image-20220115000754508" style="zoom:80%;" />

- for await (변수 of Promise배열)

  - resolve된 Promise가 변수에 담겨 나옴

  - await을 사용하기 때문에 async 함수 안에서 해야한다

    ```javascript
    const promise1 = Promise.resolve("성공1");
    const promise2 = Promise.resolve("성공2");
    (async() => {
      for await (promise of [promise1, promise2]) {
        console.log(promise);
      }
    })



##### * this

- 실행Context 내부에 ThisBinding이라는 this를 담당하는 부분이 존재하므로, this의 bingding은 해당 실행Context가 활성화 될 때 세팅
  - 실행 Context는 함수가 호출될 때 활성화 되기 때문에 this는 함수가 호출될 때 결정이 된다
  - 자바스크립트의 this는 동적으로 바인딩
  - 바인딩 : 식별자와 값을 연결하는 과정

1. 전역공간

   - 전역 객체를 참조한다
     - 브라우저 환경에서는 window가 객체
     - Node.js 환경에서는 gloabal가 객체

   ```javascript
   // 웹 브라우저에서는 window 객체가 전역 객체
   console.log(this === window); // true
   
   a = 37;
   console.log(window.a); // 37
   
   this.b = "MDN";
   console.log(window.b)  // "MDN"
   console.log(b)         // "MDN"

2. 함수 & callback 호출

   - 함수를 실행한 부분의 공간은 실질적으로 전역공간
     - 함수 호출시에는 전역객체를 가르킨다.
     - Strict mode에서는 직접 호출하면 undefined

   ```javascript
   function functionTest() { console.log(this); };
   
   functionTest(); // window {parent: Window, opener: null, top : Winodw, ...}
   ```

   - 함수를 event 처리기로 이용

     - this는 이벤트를 발사한 요소로 설정된다.

     ```javascript
     // 처리기로 호출하면 관련 객체를 파랗게 만듦
     function bluify(e) {
       // 언제나 true
       console.log(this === e.currentTarget);
       // currentTarget과 target이 같은 객체면 true
       console.log(this === e.target);
       this.style.backgroundColor = '#A5D9F3';
     }
     
     // 문서 내 모든 요소의 목록
     var elements = document.getElementsByTagName('*');
     
     // 어떤 요소를 클릭하면 파랗게 변하도록
     // bluify를 클릭 처리기로 등록
     for (var i = 0; i < elements.length; i++) {
       elements[i].addEventListener('click', bluify, false);
     }

3. 메소드 호출

   - 해당 메소드를 호출한 주체를 가르킨다.
     - 메소드 명 앞

   ```javascript
   let methodTest = {
       test: function() {
           console.log(this);
       },
   };
   
   methodTest.test(); // {test: ƒ}

4. 생성자 함수 호출

   - this가 new연산자로 생성된 인스턴스를 가르킨다.

5. 화살표 함수

   - 함수를 선언할 때 this에 바인딩할 객체가 정적으로 결정된다
     - 언제나 상위 스코프의 this를 가르킨다.
       - 화살표 함수를 정의한 객체를 나타낸다.
     - 자신이 종속된 인스턴스를 가르킨다.

- Call & Apply & Bind

  - this를 바인딩하기 위한 방법
    - this가 특정 객체를 참조하도록 만들어 준다

  1. Call

     - this를 바인딩하면서 함수를 호출한다
     - 두번째 인자를 하나씩 넘겨준다
     - 함수 호출 시 this가 가르켜야 할 주체를 명시할 수 있다
     - 첫번째 인자가 없을시 자동으로 전역 객체를 지정한다

  2. Apply

     - this를 바인딩하면서 함수를 호출한다
     - 두번째 인자가 배열이다
     - 함수 호출 시 this가 가르켜야 할 주체를 명시할 수 있다
     - 첫번째 인자가 없을시 자동으로 전역 객체를 지정한다

  3. Bind

     - this가 바인딩 된 새로운 함수를 return한다

       - 인자로 넣은 값으로 bind된다

     - 함수를 객체에 바인딩할 때 사용

       ```javascript
       let test = {
           test: function() {
               console.log(this);
           },
       };
       
       function functionTest() { console.log(this); };
       
       var bindTest = functionTest.bind(test);
       bindTest(); // {test: f}
       ```



##### * 조건부 렌더링

- 논리 연산자 `&&`, `?`를 사용하여 element를 조건부로 넣을 수 있다
- JavaScript에서 `true && expression`은 항상 `expression`으로 평가,  `false && expression`은 항상 `false`로 평가
  - 따라서 `&&` 뒤의 엘리먼트는 조건이 `true`일때 출력
- 조건부 연산자인 `condition ? true: false`를 사용

- 변수 뒤에 `?`를 넣으면 변수가 비어있는 값일 시 동작하지 않는다

  - `변수?.map`등 여러가지 경우를 생각해본다

  ```react
  movies = [1, 2, 3, 4, 5] # movies = []라면 밑에 코드는 동작X
  
  return(
    <div>
    	{movies?.map((movie) => {
    	  <div>Test입니다</div>
    	})}
    </div>
  )
  ```



##### * 주소창에 한글 입력하면 서버가 처리하지 못하는 경우 발생

- encodeURIComponent로 한글 감싸줘서 처리
- decodeURIComponent로 서버에서 한글 해석



##### * HTML 태그에 데이터를 저장하는 방법

- 서버의 데이터를 Frontend로 내려줄 때 사용
- 태그 속성으로 data-속성명
  - 속성 : id, user-job
- 자바스크립트에서 태그.dataset.속성명으로 접근 가능
  - data-user-job => dataset.userJob으로 접근
  - data-id => dataset.id로 접근
