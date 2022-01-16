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
    export default App;

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

  - App Component를 index.html(main)에서 id가 root인 것에 넣어라
  
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
         <div className='Compo'>
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
           <div className='Compo'>
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
  function App() {/* function App도 하나의 Component */}
    {
      1 < 3 ? console.log('True입니다') : console.log('False입니다')
    }
    {
      1 < 3 ?
      console.log('True입니다')
      : console.log('False입니다')
    }
    // True입니다 출력된다.
    return (
    );
  }



##### * Modal

- 삼항연산자를 활용하여 Modal을 띄운다.

  1. 조건식에는 어떤 경우에 modal창을 보여줄지에 대한 표현식 (모달창을 켜고 닫는 스위치)
  2. True일 때 띄어 줄 Modal창
  3. False일 때 띄어 줄 값 (보통 null, 텅빈 HTML)

  ```react
  {
    modal === true // 어떤 경우에 modal창을 보여줄까에 대한 조건
    ? <Modal></Modal> // Modal 창
    : null // modal을 보여주고 싶지 않을 때, 아무것도 아닌 HTML을 보내고 싶을 때(텅빈 HTML)
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
    function Modal(){
      return (
       <div className="Modal">
         <h2>제목</h2>
         <p>날짜</p>
         <p>상세내용</p>
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
    - map 반복문으로 돌린 HTML에는 key = {번호}가 필요하다
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
      return();
    }
    ```

    ```react
    function App() {
    
      let [글제목, 글제목변경] = useState(['남자가 좋아하는 음식', '살 뺄 거야', '야식 추천']);
    
      return (
        <div className="App">
          <div className="black-nav">
            <div>개발 Blog</div>
          </div>
          {
            글제목.map(function(글, i) {
              return (
                <div className="list" key={ i }>
                  <h3> { 글 }</h3>
                  <p>2022년 1월 16일 발행</p>
                  <hr/>
                </div>
              )
            })        
          }
        </div>
      );
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
         <div className="App">
           HTML 잔뜩있는 곳
           { forUI() } /* 이자리에 array에 들어있는 HTML이 표시된다 */
         </div>
       );
     }



##### * props

- App Component 안에 있는 state데이터를 다른 component에 전송할 때 사용

- Modal Component를 App Component에서 삼항연산자를 이용하여 Modal창 조작할 때, App이 부모 컴포넌트, Modal이 자식 컴포넌트

  - App이 가진 State를 Modal Component에서 바로 쓸 수 없지만, 쓸 수 있게 Modal에 전송이 가능하다

  - 자식컴포넌트는 부모 컴포넌트가 가진 state를 전송해줘야 사용이 가능하다.

    <img src="react.assets/image-20220116201539302.png" alt="image-20220116201539302" style="zoom:50%;" />

- props로 자식에게 state 전해주는 방법

  1. <자식컴포넌트 전송할변수명={전송할state}/ >

     - 전송할변수명을 보통 전송할state와 똑같이 작명한다.
       - 밑의 예시에서는 구분을 위해 다르게 표현함.

     ```react
     function App(){
       let [modal, modal변경] = useState(false);
       let [글제목, 글제목변경] = useState(['남자가 좋아하는 음식', '살 뺄 거야', '야식 추천']);
       let 그냥데이터 = 0;
       return (
       <div className="App">
         <button onClick={ ()=>{ modal변경(!modal) } }>Modal(On/Off)</button>
     	{
           modal === true
           ? <Modal 전송데이터={ 글제목 } 전송데이터2={ 그냥데이터 } ></Modal>
           : null
     	}
       </div>
       );
     }
     ```

  2. 부모컴포넌트에서 전송된 props를 인자에 입력 후 사용 (전송된 props들을 받아온다)

     - 부모에서 전달받은 props들은 인자로 적은 '전송받은props들'에 모두 들어있다.

     ```react
     function Modal(전송받은props들){
       return (
        <div className="Modal">
          <h2>{ 전송받은props들.전송데이터[0] }</h2>
          <p>날짜</p>
          <p>상세내용</p>
        </div>
       );
     }
     ```

- 제목을 누를 때 각각 다른 모달창 띄우기

  - 몇번째 제목 눌렀는지 상태정보를 state에 저장
    - 저장한 state가 0일 때 0번째 제목, 1일 때 1번째 제목 출력, 2일 때 2번째 제목 출력

  ```react
  function App(){
    let [modal, modal변경] = useState(false);
    let [글제목, 글제목변경] = useState(['남자가 좋아하는 음식', '살 뺄 거야', '야식 추천']);
    let [누른제목, 누른제목변경] = useState(0);
    return (
    <div className="App">
      <button onClick={ ()=>{ 누른제목변경(0) } }>Modal1</button>
      <button onClick={ ()=>{ 누른제목변경(1) } }>Modal2</button>
      <button onClick={ ()=>{ 누른제목변경(2) } }>Modal3</button>
            
      <button onClick={ ()=>{ modal변경(!modal) } }>Modal(On/Off)</button>
  	{
        modal === true
        ? <Modal 전송데이터={ 글제목 } 누른제목={누른제목} ></Modal>
        : null
  	}
    </div>
    );
  }
  
  function Modal(전송받은props들){
    return (
     <div className="Modal">
       <h2>{ 전송받은props들.전송데이터[전송받은props들.누른제목] }</h2>
       <p>날짜</p>
       <p>상세내용</p>
     </div>
    );
  }
  ```

  ```react
  function App() {
    let [modal, modal변경] = useState(false);
    let [글제목, 글제목변경] = useState(['남자가 좋아하는 음식', '살 뺄 거야', '야식 추천']);
    let [누른제목, 누른제목변경] = useState(0);
    return (
      <div className="App">
        <div className="black-nav">
          <div>개발 Blog</div>
        </div>
        {
          글제목.map(function(글, i) {
            return (
              <div className="list" key={ i }>
                <h3 onClick={ ()=>{ 누른제목변경(i) } }> { 글 }</h3>
                <p>2022년 1월 16일 발행</p>
                <hr/>
              </div>
            )
          })        
        }
        <button onClick={ ()=>{ modal변경(!modal) } }>Modal(On/Off)</button>
  	  {
          modal === true
          ? <Modal 전송데이터={ 글제목 } 누른제목={누른제목} ></Modal>
          : null
  	  }
      </div>
    );
  }
  
  function Modal(전송받은props들){
    return (
     <div className="Modal">
       <h2>{ 전송받은props들.전송데이터[전송받은props들.누른제목] }</h2>
       <p>날짜</p>
       <p>상세내용</p>
     </div>
    );
  }



##### * input

- 사용자가 input에 입력한 값을 state로 저장

  - Event핸들러 onChange, onInput 사용
    - **e.target**은 이벤트가 동작하는 곳을 가르킨다.
    - onChange, onInput에서 **e.target.value**은 사용자가 input에 입력한 값을 가져온다

  ```react
  function App() {
    let [입력값, 입력값변경] = useState(''); // 저장공간
    return (
      <div className="App">
        <input onChange={ ()=>{ 입력값변경(e.target.value) } } />
      </div>
    );
  }
  ```

- 글 작성(발행)

  1. 사용자가 입력한 글 변수, state로 저장
  2. 저장버튼 누르면 입력한 글 state를 다른 state에 추가
     - array.unshift() 사용 : array 맨 앞에 자료 추가하는 문법

  ```react
  function App() {
    let [입력값, 입력값변경] = useState(''); // 저장공간
    let [글목록, 글목록변경] = useState(['남자가 좋아하는 음식', '살 뺄 거야', '야식 추천']);
    return (
      <div className="App">
        <div className="black-nav">
          <div>개발 Blog</div>
        </div>
        {
          글목록.map(function(글, i) {
            return (
              <div className="list" key={ i }>
                <h3 onClick={ ()=>{ 누른제목변경(i) } }> { 글 }</h3>
                <p>2022년 1월 16일 발행</p>
                <hr/>
              </div>
            )
          })        
        }
        <div className="publish">
          <input onChange={ ()=>{ 입력값변경(e.target.value) } } />
          <button onclick={ ()=>{
              let arrayCopy = [...글목록];
              arrayCopy.unshift(입력값);
              글목록변경( arrayCopy )
            } }>저장
          </button>
        </div>
      </div>
    );
  }



##### *BootStrap

- [리액트 전용 BootStratp](https://react-bootstrap.github.io/getting-started/introduction) 존재
  - 원조 Bootstrap은 css 사이즈가 커진다.

1. react boostrap 설치

   ```
   npm install react-bootstrap bootstrap

2. react bootstrap 사이트의 CSS link 태그 index.html에 넣기

   ```
   <link
     rel="stylesheet"
     href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
     integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
     crossorigin="anonymous"
   />
   ```

3. 쓰고자 하는 곳에 react-bootstrap import하기

   - react-bootstrap에서 제공하는 것들은 모두 Component

   - 밑의 Navbar를 이용하려면 Navbar말고도 Container, Nav, NavDropdown Component를 가져와야 함

     ```react
     import React from 'react'
     import { Navbar, Container, Nav, NavDropdown } from 'react-bootstrap';
     import './App.css';
     
     function App() {
       return (
         <div className='App'>
           <Navbar bg="light" expand="lg">
             <Container>
               <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
               <Navbar.Toggle aria-controls="basic-navbar-nav" />
               <Navbar.Collapse id="basic-navbar-nav">
                 <Nav className="me-auto">
                   <Nav.Link href="#home">Home</Nav.Link>
                   <Nav.Link href="#link">Link</Nav.Link>
                   <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                     <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                     <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                     <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                     <NavDropdown.Divider />
                     <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                   </NavDropdown>
                 </Nav>
               </Navbar.Collapse>
             </Container>
           </Navbar>
         </div>
       );
     }
     
     export default App;





##### * impot/export

- export(가져오기)

  - data가 길거나 재사용성이 높은 것은 따로 보관할 파일명.js을 만들어서 App.js같은 곳에서 불러오기

    - 데이터 보관 js파일은 export default name 형식이여야 한다.

      ```react
      // data1.js
      let name = 'KimDongil';
      export default name;
      ```

    - 여러개의 데이터를 전달하려면 array, Object를 이용한다

      - Object {} 자료형 2개를 array에 저장하여 export하기 위한 예시

      ```react
      // data2.js
      export default [
        {
          name : Dongil,
          title : "나는 최고야",
          content : "나이는 27살"
        },
      
        {
          name : Kim,
          title : "내 성은 Kim",
          content : "나이는 27살"
        },
      ] 
      ```

    - 여러개의 변수를 export할 수 있다

      ```react
      // data3.js
      let firstName = 'Dongil';
      let lastName = 'kim'
      export { firstName, lastName };

  - 한 파일에 한번만 사용이 가능하다

  - Component를 파일로 관리하기

    - 파일들은 대문자로 시작하는 것으로 설정한다

    - Component 파일을 만들 때는 import React 필수

    - Component 파일이 많아지면 src내에 폴더를 만들어 관리

      ```react
      import React, {useState} from 'react'
      
      function Detail(){
        return (
          <div>나는 component가 들어있는파일</div>
        )
      }
      export default Detail;

- import(가져오기)

  - import 변수명 from 경로

    - export한 변수이름 그대로 사용하기

    ```react
    // data1.js (가져올 파일명)
    import name from ./data1.js;
    ```

    ```react
    // data2.js
    import Data from ./data2.js;
    ```

    ```react
    // data3.js
    import { firstName, lastName } from ./data3.js



### 페이지 나누기(라우팅)

- React Router 특징
  - 페이지마다 다른 HTML파일이 아니다
  - index.html 하나에 HTML 내용을 변경하면서 다른페이지처럼 보여주는 것

- 여러가지 페이지를 만들고 싶을 때는 react-router-dom 라이브러리 이용

  ```react
  npm install react-router-dom@5

- index.js에서 react-router-dom 초기셋팅법

  1. 설치한 라이브러리 import

     ```react
     import { BrowserRouter } from 'react-router-dom';
     ```

  2. App 태그를 감싸주는 BrowserRouter 태그를 생성

     - 주소창은 server에 이런 페이지좀 갖다주라고 요청하는 공간

     - BrowserRouter

       - 라우팅을 리액트가 아니라 서버에게 요청할 수도 있어서 위험하다

     - HashRouter

       - 라우팅 안전하게 할 수 있게 도와준다

       - 사이트 주소 뒤에 #이 붙는데 #뒤에 적는 것은 서버로 전달이 되지 않는다

         ```
         http://localhost:3000/#/

       - 라우팅은 리액트가 알아서 잘 해줄 수 있다

     ```react
     import React from 'react';
     import ReactDOM from 'react-dom';
     import './index.css';
     import App from './App';
     import reportWebVitals from './reportWebVitals';
     
     import { BrowserRouter } from 'react-router-dom';
     
     ReactDOM.render(
       <React.StrictMode>
         <BrowserRouter>
           <App />
         </BrowserRouter>
       </React.StrictMode>,
       document.getElementById('root')
     );
     
     reportWebVitals();

##### * Route

1. App.js에서 import

   - Link, Route, Switch 태그 불러오기

     ```react
     import { Link, Route, Switch } from 'react-router-dom'

2. App.js에서 Route태그를 이용한 페이지 나누기

   - http://localhost:3000 주소로는 main페이지

   - http://localhost:3000/detail 주소르는 detail페이지

   - 리액트 라우터는 매칭이 되는 것들을 다 보여준다 -> exact 속성사용하기

     - 경로가 정확히 일치할 때만 보여준다

     ```react
     import { Link, Route, Switch } from 'react-router-dom'
     
     function App() {
       return (
         <div className='App'>
           <Route exact path="/">
             <div>메인페이지</div> // main페이지 작업공간
           </Route>
           <Route exact path="/detail">
             <div>detail페이지</div> // detail페이지 작업공간
           </Route>
         </div>
       );
     }
     export default App;

   - Route태그 안에 component라는 속성을 통해 component를 속성값으로 집어 넣을 수 있다

     ```react
     function App() {
       return (
         <div className='App'>
           <Route exact path="/">
             <div>메인페이지</div> // main페이지 작업공간
           </Route>
           <Route exact path="/detail" component={detail}></Route>
         </div>
       );
     }
     
     function detail(){
       return (
         <div>detail페이지</div>
       )
     }
     ```

##### * Link

- 페이지 이동하기 위해 쓰는 태그

- Link태그에 to속성을 이용하여 이동한다

  - 속성값은 이동할 주소

  ```react
  <Nav.Link ><Link to="/">Home</Link></Nav.Link>
  <Nav.Link> <Link to='/detail'>Detail</Link> </Nav.Link>

##### * history

- useHistory 훅은 방문기록 등을 저장해놓은 object

  - 뒤로가기, 특정경로로 이동시키기 가능

- react-router-dom v5, react v16.3이상

- useHistory 훅 import하기

  ```react
  import React, {useState} from 'react' // useState는 useHistory를 변수에 담기위해
  import { useHistory } from 'react-router-dom';
  ```

- ex)

  - useHistory의 goback (뒤로가기)

    ```react
    // 뒤로가는 버튼 생성
    function App() {
      let history = useHistory();
      return (
        <button onClick={()=>{
      	  history.goBack();
    	}}>뒤로가기</button>
      )
    }
    ```

  - useHistory의 push

    ```react
    // 특정 경로로 이동시키기
    function App() {
      let history = useHistory();
      return (
        <button onClick={()=>{
      	  history.push('경로');
    	}}>특정경로로 이동</button>
      )
    }

##### * Switch 컴포넌트

- 리액트 라우터는 매칭이 되는 것들을 다 보여준다

- Switch는 여러개가 매칭이 돼도 하나만 매칭이 되게 해준다

  - 중복을 허용하지 않는다
  - 중복이 되면 맨 위의 Route를 선택한다

  ```react
  function App() {
    return(
      <Switch>
        <Route path="/detail">Detail</Route>
        <Route path="/:id">id</Route>
      </Switch>
    )
  }



##### 
