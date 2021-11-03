## Vue

- Front-End Development
  - HTML, CSS, JavaScript를 활용해서 데이터를 볼 수 있게 만들어 줌
    - 사용자는 데이터를 눈으로 볼 수 있고, 데이터와 상호작용 할 수 있음
  - Vue.js, React, Angular



##### * Vue.js

- 사용자 인터페이스를 만들기 위한 진보적인 자바스크립트 프레임워크

- 현대적인 tool과 다양한 라이브러리를 통해 SPA(Single Page Application)를 지원

  ![image-20211103114646269](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211103114646269.png)

  -----

  ###### SPA(단일 페이지 애플리케이션)

  - 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 Web Application
  - 단일 페이지로 구성되며 서버로부터 최초에 한번 페이지를 Download 이후 동적으로 DOM구성
    - 처음 페이지를 받은 이후부터는 서버로부터 새로운 전체 페이지를 불러오는 것이 아닌, 현재페이지 중 필요한 부분만 동적으로 다시 작성
    - 1개의 웹 페이지에서 여러 동작이 이루어지며 모바일 앱과 비슷한 형태의 사용자 경험을 제공
  - 연속되는 페이지 간의 사용자 경험(UX)을 향상
    - 트래픽의 감소와 속도, 사용성, 반응성 향상
  - 동작 원리의 일부가 CSR(Client Side Rendering)의 구조를 따름

  ###### CSR(Client Side Rendering)

  - 서버에서 화면을 구성하는 SSR 방식과 달리 클라이언트에서 화면을 구성

  - 최초 요청 시 HTML, CSS, JS 등 각종 resource(데이터 제외)를 응답받고, Client에서는 필요한 데이터만 요청해 JS로 DOM을 렌더링하는 방식

    - Server에서 뼈대만 받고 브라우저에서 동적으로 DOM을 그림

  - SPA가 사용하는 렌더링 방식![image-20211103112950955](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211103112950955.png)

  - 장점

    1. 서버와 클라이언트 간 트래픽 감소
       - Web application에 필요한 모든 정적 resource를 최초에 한 번 다운로드 후 필요한 데이터만 갱신
    2. 사용자 경험(UX)향상
       - 전체 페이지를 다시 렌더링하지 않고 변경되는 부분만을 갱신하기 때문

  - 단점

    1. SSR에 비해 전체 페이지 렌더링 시점이 느림

    2. SEO(검색 엔진 최적화)에 어려움이 있음 (최초 문서에 데이터가 없기 떄문)

  ###### SSR(Server Side Rendering)

  - Server에서 Client에게 보여줄 페이지를 모두 구성하여 전달하는 방식
  - JS 웹 프레임워크 이전에 사용되던 전통적인 렌더링 방식![image-20211103113406074](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211103113406074.png)

  - 장점
    1. 초기 구동 속도가 빠름
       - Client가 빠르게 Content를 볼 수 있음
    2. SEO(검색 엔진 최적화)에 적합
       - DOM에 이미 모든 데이터가 작성되어있기 떄문
  - 단점
    - 모든 요청마다 새로운 페이지를 구성하여 전달
      - 반복되는 전체 새로고침으로 인해 사용자 경험이 떨어짐
      - 상대적으로 트래픽이 많아 서버의 부담이 클 수 있음

  ###### SSR & CSR

  - 두 방식의 차이는 렌더링의 주최가 누구인가에 따라 결정

  - 화면을 그리는 것(렌더링)을 Server가 한다면 SSR / Client가 한다면 CSR

  - 프로젝트 구성에 맞는 방법을 적절하게 선택

    - SSR, CSR 섞는 구성가능

      ```
      Django에서 Axios를 활용한 좋아요/팔로우 로직의 경우, 대부분은 Server에서 완성된 HTML을 제공하는 구조(SSR)
      
      특정 요소(좋아요/팔로우)만 JS(AJAX & DOM조작)를 활용(CSR)
      AJAX를 활용해 비동기 요청으로 필요한 데이터를 Client에서 Server로 직접 요청을 보내 받아오고 JS를 활용해 DOM을 조작

  ###### SEO(Search Engine Optimization, 검색 엔진 최적화)

  - Web page 검색엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 Web page를 구성해서 검색 결과의 상위에 노출될 수 있도록 하는 작업
  - 구글의 등장 이후 검색엔진들이 Content 신뢰도를 파악하는 기초 지표로 사용됨
    - 다른 웹 사이트에서 얼마나 인용되었나를 반영
    - 결국 타 사이트에 인용되는 횟수를 늘리는 방향으로 최적화

  - Vue.js React 등의  SPA프레임워크는 SEO 대응이 필요한 페이지에 대해서는 선별적 SEO 대응 가능
    - 또는 추가로 별도의 프레임워크를 사용
      1. Nuxt.js
         - Vue.js 응용 프로그램을 만들기 위한 프레임워크
         - SSR지원
      2. Next.js
         - React 응용 프로그램을 만들기 위한 프레임워크
         - SSR지원

  -------

##### * Vanilla JS와 Vue.js 비교

- Vanilla JS
  1. 한 유저가 100만 개의 게시글을 작성했다 가정
  2. 이 유저가 닉네임을 변경하면, 게시글 100만 개의 작성자 이름이 모두 수정되어야 함
  3. '모든 요소'를 선택해서 '이벤트'를 등록하고 값을 변경해야 함
- Vue.js
  - DOM과 Data가 연결되어 있으면 Data를 변경하면 이에 연결된 DOM은 알아서 변경될 것
    - Data에 대한 관리만 신경쓰면 된다



##### * Vue.js의 구조

- MVVM Pattern

- Application 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴

- 구성 요소

  - Model, View, View Model

  <img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211103115421305.png" alt="image-20211103115421305" style="zoom:67%;" />

- Model
  - Vue에서 Model은 JavaScript Object
  - JavaScript의 Object 자료구조
    - Object는 Vue Instance 내부에서 data로 사용, 값이 바뀌면 View(DOM)가 바능
- View
  - Vue에서 View는 DOM(HTML)
  - Data의 변화에 따라서 바뀌는 대상
- View Model
  - vue에서 ViewModel은 Vue Instance
  - View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리
  - ViewModel을 활용해 Data를 얼마만큼 잘 처리해서 보여줄 것인지(DOM)를 고민

##### * 코드 작성 순서

- Data가 변화하면 DOM이 변경

1. Data 로직 생성
2. DOM 작성

