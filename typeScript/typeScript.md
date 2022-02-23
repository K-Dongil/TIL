## 타입스크립트

##### * TypeScript?

- 타입스크립트는 자바스크립트에 타입을 부여한 언어  (TypeScript is Typed JavaScript at Any Scale)
  - 자바스크립트의 확장된 언어
    - JavaScript의 기능들을 제공하면서 그 위에 자체 레이어를 추가
  - TypeScript는 JavaSciprt 위에 레이어로서 자리잡고 있다.
- 자바스크립트와 다르게 브라우저에서 실행하기 위해 컴파일(파일을 한번 변환)해줘야 한다



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

   ```typescript
   ex) toLocaleString() : 특정 언어의 표현 방식에 맞게 숫자를 표기하는 API
   // 만약 타입을 지정하지 않는 javaScript라고 할 때 toLocaleString을 쓰다가 오류가 난다면 브라우저에서 실행했을 때만 오류를 확인할 수 있다.
   // 타입스크립트로 작성하면 total에 타입이 지정되어 있기 때문에 해당 타입에 대한 API를 미리 보기로 띄어줄 수 있다. -> API를 일일이 치는 것이 아니라 tab으로 빠르고 정확하게 작성가능
   
   function sum(a: number, b: number): number {
     return a + b;
   }
   var total = sum(10, 20);
   total.toLocaleString();