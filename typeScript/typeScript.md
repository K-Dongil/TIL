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

- js doc & ts-check

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

   - tsc(TypeScript complie)이라고 하는  명령어를 수행하기 위해 localSystem level에 설치

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
- 프로젝트에서 tsc라는 명령어를 치면 TypeScript 설정 파일에 정의된 내용을 기준으로 컴파일 진행

1. [compilerOptions](https://typescript-kr.github.io/pages/compiler-options.html)

   - 생략될 수 있으며 생략하면 copiler의 기본값이 사용된다

   | 옵션                           | 타입      | 기본값                                                 | 설명                                                         |
   | ------------------------------ | --------- | ------------------------------------------------------ | ------------------------------------------------------------ |
   | `allowJs`                      | `boolean` | `false`                                                | js 파일들 ts에서 import해서 쓸 수 있는지 <br />JavaScript 파일의 컴파일을 허용합니다<br />(기존에 존재하는 자바스크립트 프로젝트에 타입스크립트를 점진적으로 적용할 때 사용하면 좋은 속성) |
   | `checkJs`                      | `boolean` | `false`                                                | `.js` 파일에 오류를 보고. `--allowJs`와 함께 사용<br />일반 js 파일에서도 에러체크 여부 |
   | `noImplicitAny`                | `boolean` | `false`                                                | `any` 타입 금지여부<br /> (암시한 표현식과 선언에 오류를 발생) |
   | `target`                       | `string`  | `"ES3"`                                                | TypeScript 파일을 compile 했을 때 빌드 디렉토리에 생성되는 JavaScript의 버전을 의미<br />'es3', 'es5', 'es2015', 'es2016', 'es2017','es2018', 'esnext' |
   | `module`                       | `string`  |                                                        | 모듈 코드 생성 지정<br />무슨 import 문법 쓸건지 "commonjs", "amd", "es2015", "esnext" |
   | `jsx`                          | `string`  | `"Preserve"`                                           | tsx 파일을 jsx로 어떻게 컴파일할 것인지 'preserve', 'react-native', 'react' |
   | `declaration`                  | `boolean` | `false`                                                | 컴파일시 .d.ts 파일도 자동으로 함께생성 (현재쓰는 모든 타입이 정의된 파일) |
   | `outFile`                      | `string`  |                                                        | 모든 ts파일을 js파일 하나로 컴파일해줌 (module이 none, amd, system일 때만 가능) |
   | `outDir`                       | `string`  |                                                        | js파일 아웃풋 경로바꾸기<br />출력 구조를 디렉토리로 리다이렉트 |
   | `rootDir`                      | `string`  | 공통 루트 디렉토리는 input files 리스트에서 처리됩니다 | 루트경로 바꾸기 (js 파일 아웃풋 경로에 영향줌)<br /> `outDir`로 출력 디렉토리 구조를 제어하기 위해서만 사용 |
   | `removeComments`               | `boolean` | `false`                                                | `/*!`로 시작하는 copy-right 헤더 주석을 제외한 모든 주석을 제거 |
   | `strict`                       | `boolean` | `false`                                                | 모든 엄격한 타입 검사 옵션을 활성화합니다. `strict`를 활성화하면 `noImplicitAny`, `noImplicitThis`, `alwaysStrict`, `strictNullChecks` 및 `strictFunctionTypes`이 가능 |
   | `strictNullChecks`             | `boolean` | `false`                                                | 엄격한 null 검사 모드에서는 `null`과 `undefined` 값이 모든 타입의 도메인에 있지 않고 그 자체와 `any`만 할당할 수 있습니다(한 가지 예외사항은 `undefined` 또한 `void`에 할당 가능하다는 것입니다). |
   | `strictFunctionTypes`          | `boolean` | `false`                                                | 함수파라미터 타입체크 강하게                                 |
   | `strictPropertyInitialization` | `boolean` | `false`                                                | class constructor 작성시 타입체크 강하게<br />`strictNullChecks` 활성화 필수 |
   | `noImplicitThis`               | `boolean` | `false`                                                | `any` 타입으로 암시한 `this` 표현식에 오류를 보고            |
   | `alwaysStrict`                 | `boolean` | `false`                                                | 자바스크립트 use strict 모드 켜기                            |
   | `noUnusedLocals`               | `boolean` | `false`                                                | 쓰지않는 지역변수 있으면 에러                                |
   | `noUnusedParameters`           | `boolean` | `false`                                                | 쓰지않는  매개 변수에 대한 오류                              |
   | `noImplicitReturns`            | `boolean` | `false`                                                | 함수의 모든 코드 경로에 반환값이 없을 때 오류를 보고         |
   | `noFallthroughCasesInSwitch`   | `boolean` | `false`                                                | switch문에 fallthrough 케이스에 대한 오류를 보고             |

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

6. lib

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

  - type을 object로 정의할 때 object 내부의 속성을 가져오면 오류가 발생한다

    - object안에 어떠한 속성이 들어있는 지 보장을 할 수 없다

    ```typescript
    const obj: object = {test: 1, test1:"objTest"}
    console.log(obj.test) // object 타입의 obj에는 test가 들어있는지 없는지 보장X 
    ```

  - object 내부의 속성을 사용하려면 타입을 정의할 때 object 안에 있는 속성들의 타입을 정확하게 기입

    - 객체의 모습(형상, shape)이 어떤 property(속성)으로 구성되어있는지 제대로 타입표기

    ```typescript
    const obj: {test: number, test1: string} = {test: 1, test1:"objTest"}
    console.log(obj.test) // obj에는 test가 들어있는지 알 수 있기에 오류X

- any : any

  - 알지 못하는 타입을 표현
  - 타입의 일부만 알고 전체는 알지 못할 때 유용

  ```typescript
  let notSure: any = 5;
  notSure = "string";
  notSure = true; // 성공
  
  // 여러 다른 타입이 섞인 배열에서 사용가능
  let list: any[] = [1, true, "string"]
  ```

- void : void

  - 어떤 타입도 존재할 수 없음을 나타낸다
  - void는 보통 함수에서 반환값이 없을 때 반환 타입을 표현하기 위해 쓰인다

  - void를 타입으로 사용하면 `null`과 `undefined`만 할당 가능
    - null은 `strictNullChecks`을 사용하지 않아야 할당가능

  ```typescript
  function warnUser(): void {
      console.log("No Return");
  }
  
  let unusable: void = undefined;
  unusable = null; //strictNullChecks을 사용하지 않을 때 가능



##### * 함수

- 3가지 타입 정의 가능

  - 파라미터(매개변수) 타입, 반환 타입, 구조 타입

- 타입스크립트에서는 함수의 인자를 모두 필수값으로 간주

  - 함수의 매개변수를 설정할 때 `undefined` `null`이라도 인자로 넘겨야 한다
  - compile에서 정의된 매개변수 값이 넘어왔는지 확인
    - 정의된 매개변수 값만 받을 수 있고 추가로 인자를 받을 수 없다
  - 정의된 매개변수의 갯수만큼 인자를 넘기지 않아도 되는 자바스크립트의 유연한 특성과 반대
    - 파라미터와 인자의 갯수는 1:1 mapping

- 기존 자바스크립트 함수의 선언 방식에서 매개변수와 함수의 반환 값에  타입을 추가

  - 매개변수에 타입표기
    - 매개변수를 쓰는 소괄호 안에서 변수 옆에 타입표기
  - 함수의 반환 값에 타입표기
    - 소괄호 바깥에서 반환값에 대한 타입표기
    - 함수의 반환 값에 타입을 정하지 않을 때는 `void`라도 사용

  ```typescript
  // 함수의 매개변수 타입
  function sum(a: number, b: number) {
    return a + b;
  }
  
  // 함수의 반환 타입
  function sum(): number {
    return 5;
  }

- optional parameter

  - `?`를 사용해서 정의된 매개변수의 갯수보다 적게 인자를 보낼 수 있다

    ```typescript
    function sum(a: number, b?: number): number {
      return a + b;
    }
    sum(10, 20); // 30
    sum(10, 20, 30); // error, too many parameters
    sum(10); // 10
  
- object type

  - parameter의 type을 object로 정의할 때 object 내부의 속성을 가져오면 오류가 발생한다

    - object안에 어떠한 속성이 들어있는 지 보장을 할 수 없다

    ```typescript
    function simpleTest(index: number, todo: object): void {
      todo.test = true; // object 타입의 todo에는 test가 들어있는지 없는지 보장X 
    }
    ```

  - object 내부의 속성을 사용하려면 타입을 정의할 때 object 안에 있는 속성들의 타입을 정확하게 기입

    - 객체의 모습(형상, shape)이 어떤 property(속성)으로 구성되어있는지 제대로 타입표기

    ```typescript
    function simpleTest(index: number, todo: {test: boolean, test1: number}): void {
      todo.test = true; // todo에는 test가 들어있는지 알 수 있기에 오류X
    }



##### * 인터페이스

- `interface`  `정의할이름`  `{type정의}`

- 상호 간에 정의한 약속 or 규칙

- TypeScript에서 가능한 약속 정의
  1. 객체의 스펙(속성과 속성의 타입)
  2. 함수의 파라미터
  3. 함수의 스펙(파라미터, 반환 타입 등)
  4. 배열과 객체를 접근하는 방식
  5. 클래스

- 변수를 정의하는 인터페이스

  - 변수가 정의된 인터페이스로 타입표기가 된다면, 상호 간에 정의된 규칙(interface)을 따라서 할당되어야 한다.

    ```typescript
    interface User {
      name: string;
      age: number;
    }
    
    // 변수에 사용하는 경우
    const seho: User = { name: "dongil", age: 27 };
  
- 함수의 매개변수에 인터페이스를 사용하는 경우

  - `interface`  `정의할이름`  `{type정의}`

  - 함수는 특정 형식(interface의 형식)을 준수하는 데이터만 매개변수로 받는다.

    - 인자도 특정 형식(interface의 형식)을 준수해야 한다.

    ```typescript
    interface User {
      name: string;
      age: number;
    }
    
    function getUser(user: User): void {
      console.log(user);
    }
    
    const seho: User = { name: "dongil", age: 27 };
    getUser(seho);
    
    const capt = {name: "test"}
    getUser(capt) // 오류발생

- 함수 구조(규칙, 스펙)를 정의하는 인터페이스

  - `interface`  `정의할이름`  `{(매개변수: 타입, ...): 타입}`

  - 함수의 매개변수, 반환타입을 정의할 수 있다.

    ```typescript
    // 함수의 전체 타입에 사용하는 경우
    interface SumFunction { // SumFunction이라고 하는 interface
      (a: number, b: number): number; // 매개변수와, 반환타입 정의
    }
    
    let sum: SumFunction;
    sum = function (num1: number, num2: number): number {
      return num1 + num2;
    };
    ```

- 인덱싱 방식을 정의하는 인터페이스 (배열의 인덱싱에 사용하는 경우)

  - `interface`  `정의할이름`  `{[index: index타입]: 값타입}`

  - 배열의 index에 type을 지정(속성을 부여할 때 타입 지정)

    ```typescript
    // 배열의 인덱싱에 사용하는 경우
    interface TestArray {
      [index: string]: number; // index는 string, 속성값은 number
    }
    
    let arr: TestArray;
    arr["0"] = 5;
    arr["1"] = 10;
    // arr[7] = 1; error
    ```

- 딕셔너리 패턴

  - `interface`  `정의할이름`  `{[key: key타입]: 값타입}`

  - 딕셔너의 key에 type을 지정

    ```typescript
    interface TestDictionary{
      [key: number]: string; // 정규표현식
    }
    
    const obj: TestDictionary = {
      0: "Test",
      1: "Test1",
      // "2": "Test2" error
    }
    ```


- 인터페이스 확장(상속)

  - 기존에 존재하는 interface를 상속받아 확장을 할 수 있다.

  - `interface`  `정의할이름` `extends`  `상속받을 interface`

  - extends 키워드를 이용해 상속을 받는다

    ```typescript
    interface Person {
      name: string;
      age?: number; // optional 선택자 ? 동일하게 적용 가능
    }
    
    interface Developer extends Person {
      language: string;
    }
    
    const preInterface: Person = { name: 'dongil', age: 27}
    const dongil: Developer = {
      name: 'dongil', age: 27, language: 'ts'
    };
    const dongil1: Developer = {
      name: 'dongil', language: 'ts'
    };



##### * 타입별칭(Type Aliases)

- 정의한 타입에 이름(별칭)을 부여하는 방법

  - 타입을 정의할 수 있는 모든 곳에 별칭을 붙일 수 있다

  ```typescript
  type Todo = {
    id: number;
    title: string;
    done: boolean;
  }
  ```

- 특정 type이나 interface를 참조할 수 있는 타입 변수를 의미

  ```typescript
  // string 타입을 사용할 때
  const name: string = 'capt';
  
  // 타입 별칭을 사용할 때
  type MyName = string;
  const name: MyName = 'capt';
  ```

- 타입별칭은 확장(상속)이 불가능하다

  - 좋은 소프트웨어는 언제나 확장이 용이해야 한다
  - 가급적 확장 가능한 인터페이스로 선언하면 좋다
