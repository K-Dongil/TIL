## React

##### * Why react?

- react으로 Web App 만드는 것이 가능하다.
- Web App : App이랑 사용성이 비슷한 Web
  - 다른 페이지로 넘어가거나 포스팅을 발행하거나 어떠한 행동을 할 때 새로고침X 스무스하게 동작
  - Web-App을 쉽게 만들 수 있는 라이브러리가 react
  - 장점
    1. Web app은 모바일앱으로 발행이 쉽다
       - pwa, react-native 이용
    2. 앱처럼 뛰어난 UX
    3. 뛰어난 UX로 인한 일반 웹사이트보다 비즈니스적 강점
    4. HTML 관리 용이



##### * [내가 사용한 react 세팅 & 실행](https://ko.reactjs.org/docs/create-a-new-react-app.html)

1. Node.js
   - npm 툴 사용가능
     - create-react-app 라이브러리를 이용 가능
2. Visual Studio Code (editor)

3. react 프로젝트 생성

   ```
   npx create-react-app 프로젝트명
   npx : 라이브러리 설치 도와주는 명령어
   create-react-app : 리액트 셋팅 다 된 boilerplate 설치를 도와주는 라이브러리 이름
   	boilerplate : 재사용 가능한 프로그램

4. npm start
   - 실시간으로 개발 서버를 띄어준다
5. 리액트 프로젝트에서
   - node_modules 폴더 : 라이브러리 모은 폴더
   - public 폴더 : static 파일 보관함
     - index.html : 실제 main page
   - src 폴더 : 소스코드 보관함
     - App.js :  main페이지에 들어갈 HTML 짜는 곳
     - App.css : 스타일 지정
     - index.js : App.js를 index.html에 넣어준다.
   - package.json : 설치한 라이브러리 목록
     - npm이용할 때 자동으로 등록된다



##### * 메인페이지 작동원리(App.js, index.html, index.js)

- src/App.js

  - main페이지에 들어갈 HTML 짜는 곳

  - return 소괄호 안에는 무조건 하나의 html tag만 시작하고 끝나야 한다. (하나의 요소)

    - 하나의 요소 안에 다른 태그들이 들어가있는건 괜찮다.

    ```react
    function App() {
      return (
        <div className="App">
          <p>Hello World!!</p>
        </div>
      );
    }

  - App.css

    - 스타일 적용

      ```react
      body {
        font-family:'nanumsquare';
      }
      
      .black-nav {
        background: black;
        width: 100%;
        display: flex;
        color: white;
        padding: 20px;
        font-weight: 600;
        font-size: 20px;
      }

- public/index.html

  - 실제 main page

    ```react
    <div id="root"></div>

- src/index.js

  - App.js를 index.html에 넣어준다.

  - id가 root인 Tag에 App.js안에 있는 html을 넣어라. 

    ```react
    ReactDOM.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>,
      document.getElementById('root')
    )



##### * [JSX](https://ko.reactjs.org/docs/introducing-jsx.html)

- JavaScript의 확장 문법

  - js의 모든 기능이 포함되어 있다.

- React element를 생성한다.

- JacaScirpt 코드 안에서 UI 관련 작업(HTML 작성)이 가능하다.

  - ex) JS 함수문법에서 HTML 작성이 가능

    ```react
    function App() {
      return (
        <div className="App">
          <p>Hello World!!</p>
        </div>
      );
    }

- 태그에 class 주는 법

  - class="클래스명" 대신 className="클래스명" 사용

    ```react
    function App() {
      return (
        <div className="App">
          <div className="black-nav">
            <div>개발 Blog</div>
          </div>
        </div>
      );
    }

- 데이터 바인딩

  - html 모든 곳에 중괄호 {}로 변수를 집어넣을 수 있다

    - 중괄호 안에 조건, 반복문 불가능

  - 데이터를 HTML에 넣어주는 것

    - 요소의 content, 속성값 등등 html 안에서 자유롭게 데이터 활용이 가능하다
    - 데이터 값을 변수명, 함수 등 및 중괄호{}를 이용하여 html 안에서 활용한다.

  - ex)

    ```react
    // 요소의 content에 사용
    function App() {
    
      const posts = '김동일 짱짱'
    
      return (
        <div className="App">
          <div className="black-nav">
            <div>개발 Blog</div>
          </div>
          <h4>{posts}</h4>
        </div>
      );
    }
    
    // 함수도 사용이 가능하다
    function App() {
    
      function func(){
        return 김동일
      }
    
      return (
        <div className="App">
          <div className="black-nav">
            <div>개발 Blog</div>
          </div>
          <h4>{ func() }</h4>
        </div>
      );
    }
    ```

- JSX에서 style 속성 집어넣을 때

  - style={ object자료형으로 만든 스타일 }

  - 속성명은 camelCase 작명관습을 따른다

    ```react
    // 1
    function App() {
    
      return (
        <div className="App">
          <div className="black-nav">
            <div style={{ color : "blue", fontSize : '30px'}}>개발 Blog</div>
          </div>
        </div>
      );
    }
    // 2. 스타일을 변수명에 집어넣어 데이터바인딩 이용
    function App() {
      let postCss = { color : 'blue', fontSize : '30px'}
    
      return (
        <div className="App">
          <div className="black-nav">
            <div style={ postCss } >개발 Blog</div>
          </div>
        </div>
      );
    }

- React element

  - React.createElement()를 이용한다

    ```react
    // <h1 className="greeting">Hello, world!</h1>
    // jsx 문법
    const element = React.createElement( // element같은 객체를 React 엘리먼트라 한다
      'h1',
      {className: 'greeting'},
      'Hello, world!'
    );
    
    //js 문법
    const element = React.createElement(
      'h1',
      {className:'greeting'},
      'Hello, world!'
    );
    ```



##### * state

- 데이터를 저장할 수 있는 방법
  1. 변수에 저장
  2. state에 저장
     - 웹이 App처럼 동작하게 만들기 위하여
     - state로 만들어진 data가 변경되면 HTML이 자동으로 재렌더링이 된다
     - 자주 바뀌는 변수, 중요한 데이터는 state를 사용
- 변수 대신 쓰는 데이터 저장 공간
- useState()를 이용해 만들어야 한다
- 문자, 숫자, array, object 전부 저장가능

- 사용 방법

  1. import

     - react에 있는 내장함수를 쓰겠다

     ```react
     import React, { useState } from 'react';
     ```

  2. useState 선언

     ```react
     useState('남자가 좋아하는 음식 추천');
     ```

  3. 코드 실행

     - useState는 코드가 실행되면 array[a, b]를 생성한다
     - 생성된 array[a, b]를 저장 (destructuring 문법)
       - a, b는 각 변수에 저장된다

     ```react
     let [a, b] = useState('남자가 좋아하는 음식 추천');
     실행하면 useState는 array[a, b]가 나온다.
     a : ''안에 있는 data값 (state 데이터)
     b : data인 state 정정해주는 함수 (state 데이터 변경 함수)
     
     결과 : 변수 a와 변수 b에 각각 저장된다

- state 값 수정

  - 리액트 원칙 : immutable data

  - Array, Object data 수정 방법

    1. 기존 state를 deepcopy한다
       - [...복사할 Array] {...복사할 Object data}
         - ...은 중괄호, 대괄호를 모두 제거해 달라는 의미
       - 괄호를 제거 해주었으니 다시 중괄호 또는 대괄호에 담아 새로운 Object, Array를 생성
    2. 복사본에 수정사항을 반영한다
    3. 변경함수()의 인자에 수정한 복사본을 집어넣는다
       - 변경함수(수정한 복사본)

    ##### * event를 이용한 state 값 바꾸기

    - onclick={ 실행할 함수 }
    - onclick={ (event)=>{실행할 내용} }
    - onclick의 중괄호 안에 함수명()가 아닌 함수명만 쓰기
      - 함수명()는 event가 없어도 실행 된다.

    ```react
    function App() {
    
      let [글제목, 글제목변경] = useState(['남자가 좋아하는 음식', '살 뺄 거야', '야식 추천']);
      let [따봉, 따봉변경] = useState(0)
    
      function 제목바꾸기(){
        const newArray = [...글제목]; // deepcopy
        newArray[0] = '여자가 좋아하는 음식';
        글제목변경( newArray );
      }
    
      function 따봉바꾸기(){
        let num = 따봉;
        num = num + 1;
        따봉변경(num)
      }
    
      return (
        <div className="App">
          <div className="black-nav">
            <div>개발 Blog</div>
          </div>
          <button onClick={ 제목바꾸기 }>버튼</button>
          <div className='list'>
            <h3> { 글제목[0] } <button onClick={ 따봉바꾸기 }> { 따봉 }</button></h3>
            <p>2022년 1월월 15일 발행</p>
            <hr/>
          </div>
        </div>
      );
    }





##### * Component 문법

- HTML을 줄여서 쓸 수 있는 방법

  - HTML을 한 단어로 줄여서 쓴다

- Component를 만드는 기준

  1. 반복적으로 쓰이는 HTML 덩어리들
  2. 자주 바뀌는 UI 부분 (자주 재렌더링 일어나는 부분)
     - 성능적으로 좋음

- Component 단점

  - state 쓸 때 복잡해짐
    - 상위 component에서 만든 state 쓰려면 props 문법 이용해야함

- Component 만드는 방법

  1. 함수 만들고 이름 짓기

  2. 축약을 원하는 HTML 함수 안에 넣기

  3. 원하는 곳에서 <함수명></함수명>

     ```react
     function App() {
       return (
         <div className="App">
           {/* 재사용 하고싶은 HTML 
           <div className='modal'>
             <h2>제목</h2>
             <p>날짜</p>
             <p>상세내용</p>
           </div>
           */}
     
           {/* 사용 */}
           <Compo></Compo>
     
         </div>
       );
     }
     
     function Compo(){ // 이름 짓기
       return (
         // 원하는 HTML 담기
         <div className='modal'>
           <h2>제목</h2>
           <p>날짜</p>
           <p>상세내용</p>
         </div>
       )
     }

- 유의 사항

  1. 이름은 대괄호로 시작

  2. 함수의 return() 안에는 태그 한개만 사용이 가능하다

     - 태그 하나로 묶어야 한다.

  3. return() 내부를 묶을 때 의미없이 div로 묶기 싫다면 Fragment 문법인 <></> 사용

     ```react
     function App() {/* function App도 하나의 Component */}
       return (
         <div className="App">
           {/* 사용 */}
           <Compo></Compo>
         </div>
       );
     }
     
     function Compo(){ // 이름 짓기
       return (
         // 원하는 HTML 담기
         <>
           <div className='modal'>
             <h2>제목</h2>
             <p>날짜</p>
             <p>상세내용</p>
           </div>
         </>
       )
     }



##### * 조건문

- JSX안에서 if대신 삼항연산자 이용이 가능하다.

- { 조건식 ? 참일 때 실행할 코드 : 거짓일 때 실행할 코드}

  ```react
  {
    1 < 3 ? console.log('True입니다') : console.log('False입니다')
  }
  {
    1 < 3 ?
    console.log('True입니다')
    : console.log('False입니다')
  }
  // True입니다 출력된다.



##### * Modal

- 삼항연산자를 활용하여 Modal을 띄운다.

  1. 조건식에는 어떤 경우에 modal창을 보여줄지에 대한 표현식 (모달창을 켜고 닫는 스위치)
  2. True일 때 띄어 줄 Modal창
  3. False일 때 띄어 줄 값 (보통 null, 텅빈 HTML)

  ```react
  {
      modal === true // 어떤 경우에 modal창을 보여줄까에 대한 조건
      ? <Modal></Modal> // Modal 창
      : null	// modal을 보여주고 싶지 않을 때, 아무것도 아닌 HTML을 보내고 싶을 때(텅빈 HTML)
  }

- 리액트에서는 UI를 만들 때 state 데이터를 이용한다

  1. 모달창을 켜고 다는 스위치(state데이터로 UI를 보여줄까에 대한 true/false)

     - 사이트 첫 로드시 모달창은 안보이므로 기본값은 보통 false

     ```react
     let [modal, modal변경] = useState(false);
     ```

  2. 어떠한 요소를 눌렀을 때 스위치(state 데이터)를 True로 바꿔주려한다 (Modal 띄우기 위함)

     ```react
     <h3 onClick={ ()=>{ modal변경(true) } }> { 글제목[2] }</h3>

  - ex)

    - !(느낌표) 기호는 true 왼쪽에 붙이면 false로 바꿔주고, false일 때는 true로 바꿔준다

    ```react
    function App(){
      let [modal, modal변경] = useState(false);
      return (
      <div>
        <button onClick={ ()=>{ modal변경(!modal) } }>Modal(On/Off)</button>
    	{
          modal === true
          ? <Modal></Modal>
          : null
    	}
      </div>
      );
    }



##### * 반복문

- 리액트에서는 HTML를 반복문으로 반복시킬 수 있다

- JSX 중괄호 내에 for 못 넣는다

  - map() 함수를 이용해야 한다.

- map 함수

  - 기존 array 자료형을 변형시켜 새로운 array를 만들기 위한 함수

  - array 내의 모든 데이터에 똑같은 작업을 시켜주고 싶을 때 사용

  - iterableData.map( (data) => {표현식} )

    - 반복가능한 데이터.map( () => {return HTML} )
    - return해주는 HTML에 eventListener(Onclick)이 넣어져 있어도 괜찮다
      - 다만 event에 대한 처리를 할때 주의해야 한다.
      - ex) 버튼을 클릭했을 때 값이 변경되는 event라면 state데이터를 주의해야 한다.
        - state 데이터가 반복된 HTML에서 모두 공유되어 있지 않게 해야한다.

    ```react
    function App (){
      let array = [1, 2, 3, 4, 5]
      let newArray = array.map(function(a){ // a는 array에 담긴 데이터
        return a*2
      }) // newArray는 [2, 4, 6, 8, 10]
      return()
    }

- for 반복문을 쓰고 싶다면  반복된 UI를 return 해주는 함수를 만든다

  1. 함수 안에서 for문을 쓰기위해 함수생성

  2. 비어 있는 array를 만든다

  3. for문을 이용하여 array에 HTML 추가

     - array.push(HTML);
     - for in, for of사용도 가능

  4. array를 return으로 뱉어낸다

  5. 만들어진 array를 JSX를 이용하여 보이고 싶은 자리에 사용한다.

     ```react
     function App (){
       function forUI(){
         var array = [];
         for (var i = 0; i < 3; i++) {
           array.push(<div>반복</div>)
         }
         return array
       }
       return (
         <div>
           HTML 잔뜩있는 곳
           { forUI() } /* 이자리에 array에 들어있는 HTML이 표시된다 */
         </div>
       )
     }



