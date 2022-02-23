function sumNum(a: number, b: number): number{ // 반환해주는 type까지 명시 가능
  return a + b;
}

sumNum(10, 20);

// sumNum(10, "20"); 정의 해놓은 타입이 아닌 경우 error가 발생한다. -> 코드를 돌리기 전에 미리 알 수 있다.
const result = sumNum(10, 20);
result.toLocaleString();