

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

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스

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