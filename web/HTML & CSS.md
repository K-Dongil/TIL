## HTML & CSS

[MDN(학습)]('https://developer.mozilla.org/ko/')

---

##### * Web

- 웹을 배우는 이유
  - 웹 어플리케이션 개발을 통해 SW 개발 방법 및 학습과정을 익히기 위해
  - Web은 SW개발의 기반이 되기 때문이다

- 웹 표준
  - W3C (HTML5)
  - WHATWG (HTML Living Standard)
    - Apple, Google, Microsoft, Mozlia : 브라우저를 가지고 있음
  - Can I use?
    - 내가 쓰고자하는 HTML기술이 브라우저에서 사용가능한지 확인가능
    - 쓰고자하는 기술이 다양한 브라우저에서 공통적으로 쓰일 수 있는지 확인

![image-20210802222646356](HTML%20&%20CSS.assets/image-20210802222646356.png)

- Elements - Dom 탐색 및 CSS확인 및 변경
  - styles : 요소에 적용된 CSS 확인
  - computed : 스타일이 계산된 최종 결과
  - Event Listeners : 해당 요소에 적용된 이벤트(JS)



---

---

##### * HTML

- Hyper Text Markup Language
  - Hyper : 텍스트 등의 정보가 동일 선상에 있는 것이 아니라 다중으로 연결
  - Hyer Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근
  - Markup : 특정 Text에 역할(의미)을 부여 (제목, 본문 Marking)
  - Marktup Language : 태그등을 이용하여 문서나 데이터의 구조를 명시 (데이터를 표현)
  
- 웹 페이지를 작성하기 위한(구조를 잡기 위한)언어

  ​	어떻게 구조화되어 있는지 알 수 있도록 하는 마크업 언어

  - 웹 컨텐츠의 '의미'와 '구조'를 정의

- HTML 로 작성된 문서 파일의 확장자 : .html



##### * HTML기본 구조

```
 <!DOCTYPE html> : 이 문서가 HTML5타입이다
```

- 크게 3등분

  - html요소
    - HTML 문서의 최상위 요소로 문서의 root를 뜻함 head와 body부분으로 나뉜다

  - head요소
    - 문서제목, 문자코드(인코딩)와 같이 해당 문서 정보를 담고 있다
    - 브라우저에 나타나지 않는다
    - CSS 선언 혹은 외부 로딩 파일 지정
    - meta 태그
      - charset속성을 통해 문서가 어떤 언어로 인코딩할지(해석 될지)
      - Open Graph Protocol
      - 메타 데이터를 표현하는 새로운 규약
      - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
  - body요소
    - 브라우저 화면에 나타나는 정보로 실제 내용에 해당

- DOM(Document Object Model)트리

  - 문서의 구조호된 표현 제공, 프로그래밍 언어가 DOM구조에 접근할 수 있는 방법 제공
    - 문서구조, 스타일 내용등을 표현,  저장, 조작할 수 있게 해줌

  - Web Page의 객체 지향 표현

  - 문서의 구조화된 표현을 제거하기 위해 HTML에서 사용

  - 각각의 태그를 하나의 객체로 접근하기 위해 트리로 표현

  - 들여쓰기별로 하나의 객체로 본다

    - 2spaces를 기준으로 들여쓰기
    - 문서를 접근할 때 객체단위로 접근하여 접근/수정

    ![image-20210802222855253](HTML%20&%20CSS.assets/image-20210802222855253.png)

- 요소(element)

  - HTML의 요소는 태그와 태그 사이에 위치한 내용(contents)로 구성되어 있다.

    - 태그는 보통 시작(처음)과 종료(끝) 2개로 구성되어 있다

    - 태그는 내용을 감싸는 것으로 정보의 성격와 의미를 정의

      ```
      <h1> contents </h1>
      ```

  - 내용이 없는 태그들

    - br, hr, img, input, link, meta

  - 요소는 중첩(nested)될 수 있음

    - 요소의 중첩을 통해 하나의 문서를 구조화

    - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 것이 아닌 Layout이 깨진 상태로 출력되므로 디버깅 힘들다

- 속성(attribute)

  - 태그별로 사용할 수 있는 속성은 다르다
  - 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
    - 이름(속성명)=속성값
    - 이름과 값 사이에는 공백X, 속성값에는 ""(쌍따옴표) 사용!
  - 모든 HTML 요소가 공통으로 사용할 수 있는 속성(몇몇 요소에는 아무 효과없을 수 있다)
    - id, class, hidden, lang, style, tabindex, title

- 시맨틱 태그

  - HTML5에서 의미론적 요소를 담은 태그

    - 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수 쉽다

  - 개발자, 검색엔진, 브라우저 모두에게 Contents의 의미를 명확하게 전달

    - 검색엔진 최적화(SEO)를 위해서 메타태그, 시맨틱 태그등을 통한 마크업을 효과적으로 할 필요가 있다

  - div는 의미를 가지고 있지 않으나 문서의 구조(block)를 잡기 위해서 사용하는 태그

  - 단순히 구역을 나누는 것 뿐만아니라 의미를 가지는 태그들을 활용하기 위한 노력

  - Non semantic 요소는  div, span 등이 있으며 h1, table태그들도 시맨틱 태그로 볼 수 있음

  - 대표적인 태그

    - header : 문서 전체나 색션의 헤더(머릿말)
    - nav : 내비게이션
    - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    - section : 문서의 일반적인 구분
    - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - footer : 문서 전체나 섹션의 푸터(마지막 부분)

  - 의미가 있냐 vs 없냐 (의미를 파악할 수 있나 없나?)

    ![image-20210802100935188](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20210802100935188.png)

- 시맨틱 웹
  - 웹 상에 존재하는 수많은 웹 페이지들에 메타데이터를 부여
  - 기존의 단순한 데이터의 집합이었던 웹 페이지를 "의미"와 "관련성"을 가지는 거대한 데이터베이스로 구축



##### * HTML 문서 구조화

- 인라인 / 블록 요소

  - Block 요소는 한 칸(한 줄)을 전부 차지
  - Inline 요소는 자기 데이터크기만큼만 차지

- 그룹 컨텐츠(그룹을 잡아줄 수 있는 태그?)

  ```
  <p>, <hr>, <ol>, <ul>, <pre>, <blockquote>, <div>
  ```

- 텍스트 관련 요소

  ```
  <a>
  <b> vs <strong> b: 표현상 굵게, strong : 강조
  <i> vs <em>
  <span>, <br>, <img>
  기타 등등
  ```

  - 웹 접근성 (b와 strong)
    - 장애인이나 고령자분들이 웹 사이트에서 제공하는 정보를 비장애인과 동등하게 접근하고 이용할 수 있게 보장하는 것 

- table
  - tr, td, th
- form
  - 서버에서 처리될 데이터를 제공하는 역할
  - 속성
    - action, method
  - input 
    - form안에 쓰이는 태그
    - 다양한 타입을 가지는 입력 데이터 필드
    - input 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것



---

---

##### * CSS

- Cascading Style Sheets
- 스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어

- CSS 구문

  - 선택자와 중괄호 안에 속성:값; 으로 이루어져 있다

    - 선택자를 통해 스타일을 지정할 HTML 요소를 선택

  - 속성 : 값; 을 하나의 선언(구문)이라 한다.

  - 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미

    - 속성 : 어떤 스타일 기능을 변경할지 결정
    - 값 : 어떻게 스타일 기능을 변경할지 결정

    ```
    h1 {
    	color : blue;
    	font-size : 15px;
    }
    ```

- CSS 정의 방법

  1. 인라인(inlie)

     - 해당 태그에 직접 style 속성을 활용

  2. 내부 참조

     - head 태그 내에 style태그 내에 지정

  3. 외부 참조

     - 외부에 CSS파일을 head태그내 link태그를 통해 불러오기

       ```
       <link rel="stylesheet" her="경로"></link>
       ```



##### * CSS selectors

- [CSS 연습]('https://flukeout.github.io/')

![image-20210802212727310](HTML%20&%20CSS.assets/image-20210802212727310-16279072504021.png)

- 선택자 (Selector)
  - HTML문서에서 특정한 요소를 선택하여 스타일링 하기위해서는 반드시 선택자라는 개념이 필요
  
  - 기본 선택자
    - 전체 선택자(*), 요소 선택자(HTML 태그를 직접 선택)
    - 클래스 선택자
      - 마침표(.)문자로 시작하며, 해당 class가 적용된 모든 항목을 선택
    - 아이디 선택자
      - (#)문자로 시작하며, 해당 id가 적용된 모든 항목을 선택
      - 일반적으로 하나의 문서에 1번만 사용(Unique)
        - 여러 번 사용해도 동작은하지만, 단일 id를 사용하는 것을 권장
    - 속성 선택자
    
  - 결합자(Combinators)
    - 자손 결합자
      - (띄어쓰기), 자식을 포함한 태그 안의 모든 태그들은 자손이다.
    - 자식 결합자
      - (>), 하나 아래 있는 특정 태그
    - 일반 형제 결합자, 인접 형제 결합자
    
  - nth-child(n)
  
    - 부모 요소의 모든 자식 요소중 n번째 선택
  
  - nth-of-type(n)
  
    - 부모 요소의 특정 자식 요소 중 n번째 선택
  
    - 아래 코드에서 nth-child(2)는 h2태그이나 #ssafy > p을 만족하지 못해 빨간색으로 변화하는 요소는 없다.
  
      ```
      <head>
      	<style>
      		#ssafy > p:nth-child(2){
            		color: red;
          	}
          	#ssafy > p:nth-of-type(3){
            		color: blue;
          	}
      	</style>
      </head>
      <body>
      	<div id="ssafy">
          	<h1>어떻게 선택 될까?</h1>
          	<h2>어떻게 선택 될까?</h2>
          	<p>첫번째 단락</p>
          	<p>두번째 단락</p>
          	<p>세번째 단락</p> # blue로 변화
          	<p>네번째 단락</p>
        	</div>
      </body>
      ```
  
      
  
  - 의사 클래스/요소(pseudo class)
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스



##### * CSS 우선순위

1. 중요도(Importance)

   - !important
   - 보통 쓰지 않는다

2. 운선 순위(Specificity)

   -  인라인 > id선택자 > class선택자, 속성선택자, pseudo-class > 요소 선택자, pseudo-element
   - class로만 활용해서 적용시켜야 한다.(id도 거의 안 씀)

3. 소스 순서

   - 아래 두 p태그의 Content는 둘 다 green색이다
     - 위에 써져있는 소스 순서에서 밑에 있는 style이 적용된다.

   ```
   .blue{
   	color: blue;
   }
   .green{
   	color: green;
   }
   <body>
   	<p class="blue greeen">1</p>
   	<p class="greeen blue">1</p>
   </body>
   ```



##### * CSS상속

- CSS는 상속을 통해 부모 요소의 속성 일부를 자식에게 상속

  - 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다

- 상속 되는 것 예시

  - Text관련 요소(font, color, text-align), opacity, visibility 등

- 상속 되지 않는 것 예시

  - Box model 관련요소(width, height, margin, padding, border, box-sizing, display)
  - position 관련요소 (position, top/right/bottom/left, z-index) 등

  ![image-20210802212804580](HTML%20&%20CSS.assets/image-20210802212804580.png)



##### * CSS단위

- 크기 단위
  - px(픽셀)
    - 모니터 해상도의 한 화소인 '픽셀'을 기준 (모니터 해상도에 따라 달라진다)
    - 픽셀의 크기는 변하지 않기 떄문에 고정적인 단위
  - %
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
  -  em
    - (바로 위, 부모 요소에 대한)상속의 영향을 받음
    - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
  - rem
    - (바로 위, 부모 요소에 대한)상속의 영향을 받지 않음
    - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
  - viewport
    - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역
    - 스마트폰, 태블릿 디바이스의 화면을 일컫는 용어로 사용
    - 글자 그대로 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정
    - vw, vh, vmin, vmax

- 색상 단위

  1. 색상 키워드

     - 대소문자를 구분하지 않음

     - red, blue, black과 같은 특정 색을 직접 글자로 나타냄

       ```
       p { color: black;}
       ```

  2. RGB 색상

     - 16진수 표기법(# + 16진수) 혹은 함수형 표기법(rgb(?, ?, ?))을 사용해서 특정 색을 표현하는 방식

       ```
       p { color: #????;}
       p { color: rgb(?, ?, 0);}
       p { color: rgb(?, ?, a);} # a는 alpha(투명도)
       ```

  3. HSL 색상

     - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식

       ```
       p { color: hsl(?, ?%, 0);}
       p { color: hsla(?, ?%, a);} # a는 alpha(투명도)
       ```



##### Selectors 심화

- 결합자

  - 자손 결합자
    - selectorA 하위의 모든 selectorB 요소
  - 자식 결합자
    - selectorA 바로 아래의 selectorB 요소
  - 일반 형제 결합자
    - selecotrA ~ selectorB 
    - selecotrA의 형제 요소 중 **뒤**에 위치하는  selectorB 요소를 **모두** 선택

  - 인접 형제 결합자
    - selecotrA+selectorB 
    - selecotrA의 형제 요소 중 **바로 뒤**에 위치하는  selectorB 요소를 선택



##### * CSS Box model

- 모든 HTML 요소는 box(네모) 형태로 되어있다

  - 동그라미같이 생긴 것도 결국은 box형태!!

- 하나의 박스는 네 부분(영역)으로 이루어짐

  - content, padding, border, margin

  ![image-20210802212831985](HTML%20&%20CSS.assets/image-20210802212831985.png)

- 영역은 상하좌우로 나뉜다

  - top, bottom, left, right

  - shorthand

    - 상하좌우, 상하/좌우, 상/좌우/하 , 상/우/하/좌
    - 0 auto 값을 주면 상하:0 좌우는 가운데정렬이 된다

    ![image-20210802212849894](HTML%20&%20CSS.assets/image-20210802212849894-16279073304722.png)

- box-sizing

  - 기본적으로 모든 요소의 box-sizing은 content-box
  - Padding을 제외한 순수 contents 영역만을 box로 지정

- 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함

  - box-sizing을 border-box으로 설정

    ```
    * {
    	box-sizing: border-box;
    }
    ```

    ![image-20210802212909517](HTML%20&%20CSS.assets/image-20210802212909517-16279073520743.png)

- 마진(margin) 상쇄

  - block A의 top과 block B의 bottom에 적용된 각각의 margin이 둘 중에서 큰 마진 값으로 결합(겹쳐지게)되는 현상



##### * CSS Display

- 모든 요소는 네모(박스모델)이고, 어떻게 보여지는지(display)에 따라 문서에서의 배치가 달라질 수 있다.
- display:block
  - 대표적인 블록 레벨 요소
    - div/ ul, ol, li/ p / hr/ form 등
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지 (기본이 너비의 100%)
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- display:inline
  - 대표적인 인라인 레벨 요소
    - span/ a/ img/ input, label/ b, em, i, strong 등
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지
    - 만약 다음 줄로 넘어가고 싶다면 br태그 이용
  - width, height, margin-top, margin-bottom을 지정 불가능
  - 상하 여백은 line-height로 지정
- display: inline-block
  - block과 inline 레벨 요소의 특징을 모두 갖는다
  - inline처럼 한 줄에 표시 가능
  - block처럼 width, heigth, margin 속성을 모두 지정 가능
- display: none
  - 해당 요소를 화면에 표시하지 않는다( 공간이 사라진다)
  - visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.

- 속성에 따른 수평 정렬

  - block은 margin을 이용하여 정렬

  - inline은 text-align을 이용하여 정렬

    ![image-20210802212926907](HTML%20&%20CSS.assets/image-20210802212926907.png)



##### CSS position

- 문서 상에서 요소를 배치하는 방법을 지정

- static : 모든 태그의 기본 값(기준 위치)

  - 일반적인 요소의 배치 순서에 따름(좌측 상단)

  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

- 아래는 좌표 property(top, bottom, left, right)를 사용하여 이동이 가능(음수 값도 가능)

  - position: relative (상대적)

    - **자기 자신**의 static 위치를 **기준**으로 이동

    - Layout에서 요소가 차지하는 공간은 static일 때와 같음

      - 이동은 했지만 기존 위치를 다른 요소들이 쓸 수 없음

      ![image-20210802213013130](HTML%20&%20CSS.assets/image-20210802213013130.png)

  - position: absolute (절대적)

    - 요소를 일반적인 문서 흐름에서 제거 후 Layout에 공간을 차지하지 않음

      - 원래 위치해 있었던 과거 위치에 있던 공간은 더 이상 존재X
      - 페이지의 다른 요소의 위치와 간섭하지 않는 격리된 사용자 인터페이스 기능을 만드는데 활용
        - 팝업 정보 상자, 제어 메뉴, 롤오버 패널, 페이지 어느곳에서나 끌어서 놓기 할 수 있는 유저 인터페이스 페이지 등등

    - static이 아닌 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body에 붙는 형태)

      - static이 아닌 = relative거나 absolute여야 함

      - body에 붙으면 좋지 않으므로 미리 기준(부모/조상)을 만들어놔야 좋다

        ![image-20210802213028942](HTML%20&%20CSS.assets/image-20210802213028942.png)

  
  - position: fixed (고정)
  
    - 요소를 일반적인 문서 흐름에서 제거 후 Layout에 공간을 차지하지 않음
    - 부모요소와 관계없이 viewport를 기준으로 이동(우리가 보는 화면을 기준으로)
    - 스크롤 움직여도 항상 같은 곳에 위치함