## React

##### * Why react?

- react는 Web App 만들 때 사용된다.
- Web App : App이랑 사용성이 비슷한 Web
  - 다른 페이지로 넘어가거나 포스팅을 발행하거나 어떠한 행동을 할 때 새로고침X 스무스하게 동작
  - Web-App을 쉽게 만들 수 있는 라이브러리가 react
  - 장점
    1. Web app은 모바일앱으로 발행이 쉽다
       - pwa, react-native 이용
    2. 앱처럼 뛰어난 UX
    3. 뛰어난 UX로 인한 일반 웹사이트보다 비즈니스적 강점
    4. HTML 관리 용이



##### * 내가 사용한 react 세팅 & 실행

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
   - src 폴더 : 소스코드 보관함
   - package.json : 설치한 라이브러리 목록
     - npm이용할 때 자동으로 등록된다

##### - 간단한구조(App.js, index.html, index.js)

- src/App.js

  -  main페이지에 들어갈 HTMl 짜는 곳

    ```react
    function App() {
      return (
        <div className="App">
          <p>Hello World!!</p>
        </div>
      );
    }

- public/index.html

  - 실제 main page

    ```react
    <div id="root"></div>

- src/index.js

  - App.js를 index.html에 넣어준다.

    ```react
    ReactDOM.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>,
      document.getElementById('root')
    )

