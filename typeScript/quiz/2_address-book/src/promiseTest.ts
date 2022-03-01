//동기적 코드를 실행하면 타입스크립트가 타입 추론이 가능하다
function fetchItems(): string[] {
  const items = ['a', 'b', 'c'];
  return items
}

const result = fetchItems();
console.log(result) // 결과는 result

// 비동기적 코드를 실행할 때, promise의 생성자를 실행하게 되면 Promise까지는 추론이 가능하나 그 안의 타입은 알 수 없다
// 비동기 함수를 실행하는 시점에서 타입스크립트가  Promise안에 들어오는 비동기 코드에 대해서는 알 수 없다
// 타입을 추론할 수 있는 것들은 타입스크립트 내부적으로 각각의 타입,api들이 정의되어 있기 때문이다
// 비동기 처리를 통해서 돌려받을 반환값을 명시해야 promise를 제대로 쓸 수 있다
// Promise가 기본적으로는 generic을 이용해 정의되어 있다.
// Promise 자체 타입이 generic을 받게끔 내부적으로 구현이 되어있다
function fetchItems1(): Promise<string[]> {
  const items: string[] = ['a', 'b', 'c'];
  return new Promise(function(resolve) {
    resolve(items);
  })
}
const result1 = fetchItems1();
console.log(result1) // 결과는 Promise<unknown>, 내부에 타입은 알 수 없다