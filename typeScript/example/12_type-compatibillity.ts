interface Developer{
  name: string;
  skill: string;
}
interface Person {
  name: string;
}
class Person1{
  name: string;
}
class Person2{
  name: string;
  skill: string;
  age: number;
}

let developer: Developer;
let person: Person;
// developer = person; // error
person = developer;

// developer = new Person1(); // error
developer = new Person2();

// 함수
let addFunction = function(a: number){
  // ...
}
let sumFunction = function(a: number, b: number){
  // ...
}
sumFunction = addFunction 
// addFunction = sumFunction // error

// 제네릭
interface Empty<T>{
  //...
}

let empty1: Empty<string>;
let empty2: Empty<number>;
empty1 = empty2
empty2 = empty1

// 동일한 속성은 있지만 타입이 달라지게 된다 -> 서로호환 X
interface NotEmpty<T>{
  data: T;
}
let notEmpty1: NotEmpty<string>;
let NotEmpty2: NotEmpty<number>;

// notEmpty1 = notEmpty2 // error
// notEmpty2 = notEmpty1 // error