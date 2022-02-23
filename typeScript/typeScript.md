## 타입스크립트

##### * TypeScript?

- 타입스크립트는 자바스크립트에 타입을 부여한 언어  (TypeScript is Typed JavaScript at Any Scale)
  - 자바스크립트의 확장된 언어
    - JavaScript의 기능들을 제공하면서 그 위에 자체 레이어를 추가
  - TypeScript는 JavaSciprt 위에 레이어로서 자리잡고 있다.
- 자바스크립트와 다르게 브라우저에서 실행하기 위해 컴파일(파일을 한번 변환)해줘야 한다
  - 컴파일 : ts 파일을 js 파일로 변환하는 작업



##### * Why?

1. 에러의 사전 방지

   - 변수를 생성하면서 동시에 특정 값에 할당하는 경우, 특정 값의 Type을 해당 변수의 Type으로 사용

     - Type이 무엇이 되어야 하는지 명시 가능한 JavaScript 언어의 확장을 지원

   - 객체의 형태를 명시적으로 나타내기 위해서는 interface로 선언

     ```typescript
     interface User {
       name: string;
       id: number;
     }
     ```

   - 해당 인터페이스에 맞지 않는 객체를 생성하면 TypeScript는 경고를 준다

     ```typescript
     interface User {
       name: string;
       id: number;
     }
     
     // 올바른 동작
     const user: User = {
       name: "Hayes",
       id: 0,
     };
     
     // error
     const user: User = {
       username: "Hayes",
       id: 0,
     };
     
     // error
     const user: User = {
       name: 0,
       id: 0,
     };
     ```

     ```typescript
     function sum(a: number, b: number) {
       return a + b;
     }
     sum('10', '20'); // Error: '10'은 number에 할당될 수 없습니다.
     ```

   - 자바스크립트는 경고를 주지 않는다

     ```javascript
     function sum(a, b) {
       return a + b;
     }
     sum('10', '20'); // 1020

2. 코드 가이드 및 자동 완성(개발 생산성 향상)

   - javaScript는 코드를 작성하는 시점에 변수의 타입을 인지할 수 없다.
     - 개발자가 스스로 결과를 예상하고 타입을 가정한 상태에서 코딩을 하게 된다.
   - visual Studio의 intellisense(자동 완성)이 편해진다.

   ```typescript
   ex) toLocaleString() : 특정 언어의 표현 방식에 맞게 숫자를 표기하는 API
   // 만약 타입을 지정하지 않는 javaScript라고 할 때 toLocaleString을 쓰다가 오류가 난다면 브라우저에서 실행했을 때만 오류를 확인할 수 있다.
   // 타입스크립트로 작성하면 total에 타입이 지정되어 있기 때문에 해당 타입에 대한 API를 미리 보기로 띄어줄 수 있다. -> API를 일일이 치는 것이 아니라 tab으로 빠르고 정확하게 작성가능
   
   function sum(a: number, b: number): number { // 반환해주는 type까지 명시 가능
     return a + b;
   }
   var total = sum(10, 20);
   total.toLocaleString();



##### * 자바스크립트를 타입스크립트처럼 코딩하는 방법

- js doc & generic & ts-check

  ![image-20220223111201447](typeScript.assets/image-20220223111201447.png)

  ```javascript
  // @ts-check
  
  /**
   * @param {number} a 첫번째 숫자
   * @param {number} b 두번째 숫자
   */
  
  function sum1(a, b){
    return a + b;
  }
  
  sum1(10, 20);
  
  // javaScript는 밑에와 같은 오류를 미리 알려주지 않는다.
  // @ts-check를 사용하면 javaScript에서도 오류를 알려줄 수 있다. 
  sum1(10, "20");
  ```



##### * typeScript complie

- typeScript는 브라우저에서 실행되기 위해서는 컴파일 작업이 필요하다
- ts확장자 파일을 js로 변환해주는 complie 작업을 반복하지 않기 위해서는 webpack이용 

1. node기반으로 사용하는 자바스크립트 라이브러리를 설치

   - tsc(typeScript complie)이라고 하는  명령어를 수행하기 위해 localSystem level에 설치

   ```
   npm install typescript -g
   ```

2. ts확장자 파일을 js로 변환해주는 complie 작업

   ```
   tsc 파일명.ts
   ```

3. complie 작업 완료 후 js확장자 파일이 생긴다.



##### * typeScript 설정 파일

- 디렉토리에 tsconfig.json파일이 있따면 해당 디렉토리가 TypeScript 프로젝트의 루트가 된다.

- tsconfig.json 파일의 경로를 명시적으로 지정

  ```
  tsc --project 상대경로
  tsc -p 상대경로

- typeScript를 javaScript로 변환할 때의 설정을 정의해놓는 파일
  - complie 작업할 때 부가적인 옵션 부여
- 프로젝트에서 tsc라는 명령어를 치면 typeScript 설정 파일에 정의된 내용을 기준으로 컴파일 진행

1. compilerOptions

   - 생략될 수 있으며 생략하면 copiler의 기본값이 사용된다

   | 옵션                   | 타입      | 기본값   | 설명                                                         |
   | ---------------------- | --------- | -------- | ------------------------------------------------------------ |
   | `--allowJs`            | `boolean` | `false`  | JavaScript 파일의 컴파일을 허용합니다<br />(기존에 존재하는 자바스크립트 프로젝트에 타입스크립트를 점진적으로 적용할 때 사용하면 좋은 속성) |
   | `--checkJs`            | `boolean` | `false`  | `.js` 파일에 오류를 보고. `--allowJs`와 함께 사용            |
   | `-noImplicitAny`       | `boolean` | `false`  | `any` 타입으로 암시한 표현식과 선언에 오류를 발생시킵니다.   |
   | `--charset`            | `string`  | `"utf8"` | 입력 파일의 문자 집합입니다.                                 |
   | `--diagnostics`        | `boolean` | `false`  | 진단 정보를 보여줍니다.                                      |
   | `--downlevelIteration` | `boolean` | `false`  | ES5 또는 ES3를 대상으로 할 때 `for..of`, 스프레드와 구조분해할당에서 이터러블을 완전히 지원합니다. |

2. files

   - TypeScript 변환 명령어를 입력할 때 마다 대상 파일의 경로를 지정하지 않고 설정 파일에 미리 정의
   - 컴파일 대상 경로를 정의하는 속성의 우선 순위
     - files > include = exclude

   ```typescript
   {
     "files": ["app.ts", "./utils/math.ts"]
   }

3. include

   - files와 같이 파일을 개별로 지정하지 않고 include 옵션으로 변환할 폴더를 지정할 수 있다

   ```typescript
   {
     "include": ["src/**/*"]
   }
   
   // 와일드 카드 패턴
   * : 해당 디렉토리의 모든 파일 검색
   ? : 해당 디렉토리 안에 파일의 이름 중 한 글자라도 맞으면 해당
   ** : 하위 디렉토리를 재귀적으로 접근(하위 디렉토리의 하위 디렉토리가 존재하는 경우 반복해서 접근)
   ```

4. exclude

   - include와 반대로 변환하지 않을 폴더 경로를 지정
   - 설정하지 않을 시 기본적으로 node_modules, browser_components 같은 폴더를 제외

   ```typescript
   {
     "exclude": ["node_modules"]
   }
   ```

5. extends

   - 특정 TypeScript 설정 파일에서 다른 TypeScript 설정의 내용을 가져와 추가할 수 있는 속성
   - 확장자 파일의 내용을 가져다가 덮어쓰거나 새로 정의할 수 있다

   ```typescript
   // config/base.json
   {
     "compilerOptions": {
       "noImplicitAny": true
     }
   }
   
   // tsconfig.json
   {
     "extends": "./config/base"
   }
   ```

6. target

   - TypeScript 파일을 compile 했을 때 빌드 디렉토리에 생성되는 JavaScript의 버전을 의미한다
     - 기본값인 ex3부터 es6 등 esnext까지 존재

   ```typescript
   {
     "target": "esnext"
   }
   ```

7. lib

   - TypeScript 파일을 JavaScript로 compile할 때 포함될 라이브러리의 목록

   ```typescript
   // ex) async 코드를 complie 할 때 Promise 객체가 필요하므로 아래와 같은 설정이 필요
   // es2015는 프로미스 객체를 타입스크립트에서 인식할 수 있게 필요한 속성
   // dom 관련 속성은 DOM API를 사용하는 경우 필요
   {
     "lib": ["es2015", "dom", "dom.iterable"]
   }



##### * 변수타입

- 타입표기

  - `:`를 이용하여 javaScript  코드에 type을 정의하는 방식

- 문자열 : string

  ```typescript
  const str: string = "hello";
  ```

- 숫자 : number

  ```typescript
  const num: number = 5;
  ```

- 진위값 : boolean

  ```typescript
  const bool: boolean = true;
  ```

- 배열 : Array

  ```typescript
  const arr: number[] = [1, 2, 3]; // 배열안에 숫자타입만 들어갈 수 있다
  
  // 제네릭 사용
  const arr1: Array<string> = ["1", "2", "3"]; // 배열안에 문자열 타입만 들어갈 수 있다 
  ```

- 튜플 : [type1, type2]

  - 배열의 길이가 고정되고 각 요소의 타입이 지정되어 있는 배열 형식
  - 정의하지 않은 타입, 인덱스로 접근할 경우 오류발생

  ```typescript
  const arr: [string, number] = ["hello", 10];
  ```

- 객체 : object

  ```typescript
  const obj: object = {};
  
  // object안에 특정 속성과 속성의 값들 까지 정의
  const obj: {name: string, age: number} = {
    name: "dongil",
    age: 27
  }
  ```



