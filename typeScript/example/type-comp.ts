// 인터페이스
interface Developer {
  name: string;
  skill: string;
}

interface Person {
  name: string;
}

var a: Developer;
var b: Person;
// a = b; // X
b = a; // O

// 함수
var add = function(a: number) {
  // ...
}
var sum = function(a: number, b: number) {
  // ...
}
sum = add; // O
// add = sum; // X

// // 유니온 타입
var c: Developer | Person;
var d: Person | string;
// c = d; // X
d = c; // O