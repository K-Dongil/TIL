// 자바스크립트 함수 선언
// function sum(a, b) {
//   return a + b;
// }

// 타입스크립트 함수 선언 - 함수의 매개 변수
function sum(a: number, b: number) {
  return a + b;
}

// 타입스크립트 함수 선언 - 함수의 반환 타입
function sum1(a: number, b: number): number {
  return a + b;
}

// function add(a: number, b: number): string {
//   return a + b;
// }

// 함수 인자
function log(a: string) {
  console.log(a);
}
log('a', 10); // javaScript와 다르게 정해진 매개변수보다 인자가 더 존재할시 오류

// 함수 옵셔널 파라미터(optional parameter)
function printText(text: string, type?: string) {
  console.log(text);
}
printText('hi');
