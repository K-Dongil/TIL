##### * ReactJS와 무엇이 다른지?

- ReactJS에는 있는 ReactDOM.render가 없다

- 리액트는 client-side render

  - 사용자의 행동에 따라 필요한 부분만 다시 읽어들인다

  - page 전체를 요청하지 않고 페이지에 필요한 부분만 변경한다

    - 모바일 네트워크에서도 빠른 속도로 렌더링 가능

  - lazy loading 지원

  - 브라우저가 자바스크립트를 가져와서, Client-Side의 자바스크립트가 모든 UI를 만든다

    1. 브라우저가 HTML을 가져올때 비어있는 div를 가져온다
    2. 브라우저가 모든 자바스크립트를 요청한다
    3. 브라우저가 자바스크립트와 react.js를 실행한다
    4. 앱이 유저에게 보여진다(UI 만들어짐)

    - 유저가 보는 것은 <div id="root"></div> 이 부분
    - 유저가 브라우저에서 자바스크립트를 비활성하면 noscript 태그를 본다

  - Server Side Rendering이 따로 필요X, 일관성 있는 코드 작성 가능

  - 페이지를 읽고, 자바스크립트를 읽은 후 화면을 그리는 시간까지 모두 마쳐야 콘텐츠가 사용자에게 보여지기 때문에 초기구동 속도가 느리다

- NextJS는 Server Side Rendering

  - 사용자가 처음으로 컨텐츠를 볼 수 있는 시점을 앞당길 수 있다
  - next.js는 초기 상태로 pre-rendering한다
    - html은 app의 initial state(초기 상태)
  - hydration
    - next.js는 react.js를 백엔드에서 동작시켜서 페이지를 미리 만든다
      - component를 렌더링? -> HTML?
    - 자바스크립트와 react.js가 로딩되지 않았더라도 콘텐츠를 볼 수 있다
  - 유저가 웹사이트에 가면, 초기 상태의 component로 미리 생성된 HTML 페이지를 보게되고 상호작용이 일어나면 react.js는 그걸 받아서 작동?????
  - 검색엔진최적화(SEO) 적용이 용이하다
  - 모든 요청에 관해 필요한 부분만 수정X, 완전히 새 페이지를 로딩하고 render(새로고침)
  - 전체를 로딩하므로 CSR보다 느리고, bandwidth를 많이쓰고 사용자경험이 좋지 않다

- NextJS의 어딘가의 코드가 이걸 하고 있다

  - 추상화 작업이 되어있다



##### * framework(NextJS)와 library(ReactJS)의 차이

- library는 개발자가 불러와서 직접 사용해 작업을 한다
  - 개발자가 원할 때 부르고 원할 떄 사용이 가능하다
- framework는 개발자가 작성한 코드를 모든 걸 동작하게 한다
  - 특정한 규칙을 따르면 정상적으로 돌아가게 해준다
  - 정해진 규칙에, 개발자가 코드를 적절한 곳에 넣어준다면 framework가 코드를 불러서 사용한다
  - 규칙을 수정할 수 없다



##### * 시작

- NextJS프로젝트 생성

  ```
  npx create-next-app@latest
  ```

- NextJs + TypeScript 프로젝트 생성

  ```
  npx create-next-app@latest --typescript

- 프로젝트 실행

  ```
  npm run dev
  ```



##### * NextJS의 장점

- url
  - 파일명으로 url mapping
- jsx사용
  - jsx를 사용할 때 React.js를 import하지 않아도 된다
- 앱에 있는 페이지들이 미리 렌더링



##### * pages

- url (NextJS의 route)

- `index.js`
  - `/` (기본 url)
  - `pages`에서 `index.js`
    - 프로젝트의 홈페이지로 연결
      - localhost:3000 (O), localhost:3000/index (X)
  - 특정 폴더 안에서 `index.js`는 특정 폴더의 url를 가진다
    - ex) `pages >> test 폴더 >> index.js`
      - localhost:3000/test

  - pages 폴더에 react.js component를 export하고 있는 파일을 pages 폴더 안에 두면 next.js가 파일의 이름을 가져다가 url의 이름으로 쓴다
    - 파일의 이름이 중요, component의 이름은 연관X
    - export default로 export하지 않으면, react component가 아니라는 에러가 뜬다



##### * Dynamic Routes

- 파일 이름에 대괄호 사용
  - 현재 페이지가 동적으로 라우팅 된다는 것을 인식할 수 있다
  - 동적 라우팅에 대괄호로 지정된 임의의 이름은 라우터 객체의 query 속성으로 들어간다

- 파일 이름을 `[Code에서 사용하고자 하는 변수명].js`로 만든다



##### * catch-all URL

- 뭐든 캐치해내는 URL

- `[...변수명].js` ...을 통해 url의 특정 부분 뒤의 data값들을 `/`를 구분으로 query로 받아온다

  - 접근한 url에서 parameter값들을 사용하기 위해서는 아래와 같이 접근

    ```react
    const router = useRouter();
    
    const [title, id] = router.query.params || [];
    ```

- SEO에 최적화하기 위한 코드 작성예시 (Detail Page)

  - 컴포넌트 내부에 들어있는 router는 클라이언트 사이드에서만 실행이 된다
  - getServerSideProps 사용
    - URL에 들어있는 parameter를 사용해서 구글 SEO에 최적화시키기

  ```react
  // http://localhost:3000/movies/영화이름/영화번호
  // 파일명 : [...params].js
  export default function Detail({params}) {
    const [title, id] = params || [];
    return (
      <div>
        <h4>{title}</h4>
      </div>
    );
  }
  
  export function getServerSideProps({params:{params}}){
    return {
      props: {
        params
      },
    };
  }
  ```





##### * Link, useRouter

- Link 태그에 href로 움직일 경로 지정

- content부분에 a태그 및 스타일 지정

  - Link 태그에 스타일 지정이 안 된다. (React.js랑 다르다..?)

  ```react
  import Link from "next/link";
  import { useRouter } from "next/router";
  
  export default function NavBar(){
    
    return (
      <nav>
        <Link href="/">
          <a style={{color: router.pathname === "/" ? "red" : "blue"}}>Home</a>
        </Link>
        <Link href="/about">
          <a style={{color: router.pathname === "/about" ? "red" : "blue"}}>About</a>
        </Link>
      </nav>
    )
  }



##### * NextJS에서 style을 적용하는 2가지 방법

1. CSS Modules 패턴
2. styles JSX



##### * CSS Modules 패턴

- 파일명.module.css

- className을 추가해줄 때 className을 text로 적지 않는다

  - 자바스크립트 오브젝트에서의 property 형식으로 적는다

- 태그에 여러개의 className을 적용

  - 백틱 사용

    ```react
    import test from "./Test.module.css";
    
    <p className=`${test.something1} ${test.something2}` />
    ```

  - 배열과 join() 사용

    ```react
    import test from "./Test.module.css";
    
    <p className={ [test.something1, test.something2].join(" ") } />

- 파일명.module.css에서 만든 css를 import해와서 className에 적용할 때, 무작위 text가 만들어져 지정된다.

  - 재사용할 때 중복이 되지않아 충돌이 일어나지 않는다 (클래스 이름 충돌 방지)

  ```react
  // NavBar.module.css
  .active {
    color: tomato;
  }
  
  ==============================================================
  
  import Link from "next/link";
  import { useRouter } from "next/router";
  import customStyles from "./NavBar.module.css";
  
  export default function NavBar(){
    const router = useRouter();
    return (
      <nav>
        <Link href="/">
          <a className={router.pathname === "/" ? customStyles.active : ""}>
            Home
          </a>
        </Link>
        <Link href="/about">
          <a className={router.pathname === "/about" ? customStyles.active : ""}>
            About
          </a>
        </Link>
      </nav>
    )
  }



##### *styled JSX

- style 태그, jsx, prop이용한다

  ```react
  <style jsx>
    {`
      cssSelect {
        속성: 속성값;
      }
      cssSelect {
        속성: 속성값;
      }
    `}
  </style>
  ```

- 작성한 style은 작성한 module안에서만 적용되고 다른 module에 영향을 주지 않는다

  - 독립적이다
  - style은 컴포넌트 내로 한정 되어 있다.

- 태그를 선택해서 style을 주면 브라우저에서 확인할 때 className이 무작위로 생성되어 적용되는 것을 확인할 수 있다

- 조건에 따른 style 적용하는 방법

  - 삼항연산자를 이용하여 태그에 className(혹은 id)을 적용한 다음 styled JSX에서 CSS Selector을 이용해서 style 지정

    ``` react
    // styled JSX
    import Link from "next/link";
    import { useRouter } from "next/router";
    
    export default function NavBar(){
      const router = useRouter();
      return (
        <nav>
          <Link href="/">
            <a className={router.pathname === "/" ? "active" : "not_active"}>
              Home
            </a>
          </Link>
          <style jsx>
            {`
              .active {
                color: blue;
              }
              .not_active{
                color: red;
              }
            `}
          </style>
        </nav>
      )
    }

- `global`
  - styles를 global(전역)에 추가하고 싶을 때
  - 한 페이지에서 global을 줘서 Component에 styles를 적용해도 다른 페이지에서 똑같은 Component를 불러왔을 때, 다른페이지에서 불러온 Component에 대해서는 적용X



##### * Custom App

- pages에서 `_app.js` 파일을 만든다

  - NextJs는 page 파일이 렌더링 되기 전에 `_app.js`을 먼저 불러온다
    - NexJS는 `_app.js`에 있는 함수를 불러온다
  - `_app.js`라는 이름은 NextJs가 이 파일을 보기위한 지정(약속)된 방식
  - `_app.js`는 가장 먼저 실행되는 컴포넌트로 각 페이지에 공통적으로 들어가는 부분을 처리하기에 좋다.

- 두 개의 props가 존재한다

  1. Component
     - page
  2. pageProps
     - getServerSideProps

  ```
  export default function App({Component, pageProps}){ ....... }

- 받아온 Component, pageProps 및 다른 값들도 추가가능, 새로운 Component를 반환

  - 리액트의 hoc와 비슷하다

  ```react
  import NavBar from "../component/NavBar";
  
  export default function App({Component, pageProps}){
    const test = "Hello";
    return (
      <div>
        <NavBar />
        <Component {...pageProps} />
        <span>Test</span>
      </div>
    )
  }

- 모든 페이지에 styles를 적용할 수 있게 해준다
  - global css
    - `styles/globals.css`파일은 `_app.js`파일에서만 import가 가능하다



##### * Head 태그

- 해당 페이지에 대한 정보를 담고 있는 태그
- NextJs의 경우 자동으로 head가 만들어진다
  - 따로 변경하기 위해서는 next안에 있는 Head 컴포넌트를 사용



##### *  public 파일 (img, svg 등...)

- public 디렉토리(폴더)에서 관리
- pages 또는 component에서 가져다 쓸 때, src의 속성값에 `/파일이름.확장자`만 써주면 된다



##### * image

- NextJS에서는 img 태그 대신에 image 태그를 쓴다
  - Next.js의 Image 태그는 최신 웹용으로 확장된 next/imageHTML img요소
  - 브라우저에서 지원하는 경우 JPEG보다 약 30 % 작은 WebP와 같은 최신 이미지 형식으로 이미지를 자동으로 제공
    - 필요에 따라 이미지 최적화
  - 뷰포트를 스크롤하는 동안 특정 임계 값에 도달 한 경우에만 페이지 내부의 이미지를 지연로드
  - 동적으로 사용할 다양한 및 사용자 정의 해상도에 대해 다른 이미지 크기를 지정가능
  - 사진의 품질을 75 %로 설정된 낮은 임계 값으로 자동 변경
    - 각 호출에 대해 변경이 가능하다
  - image component는 로컬이미지, 원격이미지를 사용할 때 복잡해 질 수 있다
    - public, backend에서 받아서 사용하는 이 외에는 오류가 발생



##### * useState와 map의 사용

- useState로 정의되는 값을 이용해서 map을 적용하려고하면 useState의 초기값을 지정해줘야 한다
  - useState의 초기값이 비어있다면 NextJS의 특성(SSR) 때문에 오류가 난다



##### * Redirect

- 특정 url에 접근했을 때 다른 url로 redirection해준다.

- `next.config.js`에서 설정

  - `redirects() { return [ { source, destination, permanent}] }`

- NextJS가 redirectrion을 허용한다

- `source` : 접근한 page url

  - url에 `*`이 붙으면 비슷한 특정 url에 한해서는 모두 redirect

- `destination` : source url에 접근했을 때 redirection할 url

  - url에 `*` 이 붙으면 source의 url에 붙어있던 parameter들을 전부 가져와 redirect하는 url에도 붙인다

- `permanent` : boolean, 브라우저나 검색엔진이 redirect한 정보를 기억하는지 여부를 결정

  ```react
  module.exports = {
    reactStrictMode: true,
  
    async redirects() {
      return [
        {
          source: "/old-blog/:path*",
          destination: "/new-blog/:path*",
          permanent: false,
        },
      ];
    }
  };
  ```



##### * Rewrite

- 특정 url에 접근했을 때 redirect를 해주지만 url은 바뀌지 않는다
  - NextJS가 request를 masking
    - 서버 뒤에 mask되어 가려져 있다

- `next.config.js`에서 설정

  - `rewrites() { return [ { source, destination, permanent}] }`

  ```react
  const API_KEY = "10923b261ba94d897ac6b81148314a3f";
  
  module.exports = {
    reactStrictMode: true,
  
    async rewrites() {
      return [
        {
          source: "/api/movies",
          destination: `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`
        },
      ];
    }
  };



##### * get Server Side Props

- page를 사용하는 유저에게 로딩 단계를 보여주고 싶지않고, SEO에 최적하게 만들어준다

- NextJS가 html 형태로 export (pre render)해준다

  - html은 app의 initial state(초기 상태)

- `getServerSideProps` 함수 안에서 쓰는 코드는 server에서 동작(돌아간다)

  - client쪽이 아닌, server쪽에서만 작동
  - return으로 반환해주는 값은 props로써 page, component에게 전달한다
    - getServerSideProps -> _app.js -> page, component
    - `_app.js`에서 props를 받아서 component(page)에 props 전달

  ```react
  // _app.js
  export default function App({Component, pageProps}){
    const test = "Hello";
    return (
      <div>
        <Component {...pageProps} />
      </div>
    )
  }
  
  // index.js
  export default function Home({ results }) {
    return (
      <div className="container">
        
        {results?.map((movie) => (
          <div className="movie" key={movie.id}>
            <img src={`https://image.tmdb.org/t/p/w500/${movie.poster_path}`} />
            <h4>{movie.original_title}</h4>
          </div>
        ))}
      </div>
    )
  }
  
  export async function getServerSideProps() {
    const { results } = await (
      await (await fetch(`https://api.themoviedb.org/3/movie/popular?api_key=10923b261ba94d897ac6b81148314a3f`)).json()
    )
    return {
      props: {
        results,
      },
    };
  }



##### * Layout Patterns

- custom app component를 사용할 때 자주 사용된다

- Component를 props로 보내서 사용한다

  ```react
  // index.js
  export default function Home({ results }) {
    return (
      <div className="container">
        
        {results?.map((movie) => (
          <div className="movie" key={movie.id}>
            <img src={`https://image.tmdb.org/t/p/w500/${movie.poster_path}`} />
            <h4>{movie.original_title}</h4>
          </div>
        ))}
      </div>
    )
  }
  
  export async function getServerSideProps() {
    const { results } = await (
      await (await fetch(`https://api.themoviedb.org/3/movie/popular?api_key=10923b261ba94d897ac6b81148314a3f`)).json()
    )
    return {
      props: {
        results,
      },
    };
  }
  
  // _app.js
  import Layout from "../component/Layout";
  
  export default function App({Component, pageProps}){
    const test = "Hello";
    return (
      <div>
        <Layout>
          <Component {...pageProps} />
          <div>Test</div>
        </Layout>
      </div>
    )
  }
  
  // Layout.js
  export default function Layout({children}) {
    return (
      <>
        <div>{children}</div>
      </>
    )
  }



##### * URL에서 URL로 state를 넘겨주고 유저에게 숨기는 방법

- `as`속성이 브라우저의 URL을 masking(숨겨준다)

  ```react
   <Link
    href={{
      pathname: `/movies/${movie.id}`,
      query: {
  	  title: movie.original_title,
      },
    }}
    as={`/movies/${movie.id}`}
  >
    <a>{movie.original_title}</a>
  </Link>

- push로 url을 이동시킬 때 숨겨주는 방법

  ```react
  const router = useRouter();
  
  router.push(
    {
      pathname: `접근 URL`,
      query: {
        url로 보낼 값,
      },
    },
    `masking할 URL`
  );



##### * 404 page

- 파일이름을 `404.js`로 만들어준다.

  ```react
  export default function NotFound() {
    return "잘못된 url 접근입니다!!";
  }
