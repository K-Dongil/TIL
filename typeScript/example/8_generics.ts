function logText(text){
  console.log(text);
  return text;
}
logText(10); // 숫자 10
logText('hi'); //문자열 hi
logText(true); // 진위값 true

function genericLogText<T>(text: T):T{
  console.log(text);
  return text
}
genericLogText<string>('hi'); // 파라미터의 타입은 문자열, 함수를 호출하는 시점에 타입을 넘겨준다

function genericLogText1(text){
  console.log(text);
  return text;
}
genericLogText1(10); // 숫자 10
genericLogText1('hi'); //문자열 hi
genericLogText1(true); // 진위값 true


function getNumber(value: number) {
  return value;
}

function getArray(value: string[]) {
  return value;
}

// 제네릭 기본 문법 - 함수
function getValue<T>(value: T): T {
  return value;
}
getValue<string>('hi').toLocaleUpperCase();
getValue<number>(100).toLocaleString();

// 제네릭 기본 문법 - 인터페이스
interface Developer<T> {
  name: string;
  age: T;
}
const tony: Developer<number> = { name: 'tony', age: 100 };

interface Dropdown {
  value: string;
  selected: boolean;
}

const obj: Dropdown = {value: 'abc', selected: false};

interface DropdownGeneric<T> {
  value: T;
  selected: boolean;
}

const obj1: DropdownGeneric<string> = {value: 'abc', selected: false };

// 제네릭 타입 제한 - 구체적인 타입
function getNumberAndArray<T>(value: T): T {
  value.length; // X
  return value;
}
getNumberAndArray<string>('hello')

function getNumberAndArray1<T>(value: T[]): T[] {
  value.length; // O
  value.forEach(function(value){
    console.log(value)
  })
  return value;
}
getNumberAndArray1<string>(['hello'])

// 제네릭 타입 제한 - 정의된 타입 이용하기
interface LengthType {
  length: number;
}

function logTextLength<T extends LengthType>(text: T):T {
  text.length;
  return text
}
logTextLength('abc')


// 제네릭 타입 제한 - keyof
interface ShoppingItems {
  name: string;
  price: number;
  address: string;
  stock: number;
}
function getAllowedOptions<T extends keyof ShoppingItems>(option: T): T {
  if (option === 'name' || option === 'address') {
    console.log('option type is string');
    return option;
  }
  if (option === 'price' || option === 'stock') {
    console.log('option type is number');
    return option;
  }
}
getAllowedOptions('name');
// const a = getAllowedOptions('name');
// a.toUpperCase(); // Name