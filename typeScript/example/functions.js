// 자바스크립트 함수 인자 특성 (유연함)
function sum(a, b) {
  return a + b;
}

console.log(sum(10, 20, 30, 40, 50)); // 30, 40, 50은 무시된다
