function solution(n) {
  let answer = 0;
  for (let i = 1; i<=(n**(0.5)); i++){
      if (n%i){
          continue
      }
      answer += i
      answer += (n/i) == i ? 0 : n/i
  }
  return answer;
}