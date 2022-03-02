// 중간에 연산이나 복잡한 코드들에 의한 바뀐 값에 대해서는 타입추론 불가, 추적불가
let a;
a = 20;
a = 'a';
let b = a; // 맨 처음 선언 된 타입을 b에 할당하고 있다

// 타입단언(type assertion)
// 타입 스크립트보다 개발자가 타입을 더 잘 알고 있으니 타입스크립트는 신경X, 개발자가 정의한 타입을 받아들이게 한다
let c;
c = 5;
c= 'hello';
let d = c as string;

// DOM API 조작
// <div>hello</div>
const div = document.querySelector('div'); // querySelector로 접근하는 시점에 document.querySelector가 돌아가는 라인 시점에서 div가 있다는 보장을 해주지 않기 때문에 
// 타입에 대한 값을 보장해줘야 한다
if (div) { // document.querySelector('div')은 HTMLDivElement 혹은 null 타입을 준다
  div.innerText
}

// as를 쓰는 시점에서는 
const div1 = document.querySelector('div') as HTMLDivElement;
div1.innerText