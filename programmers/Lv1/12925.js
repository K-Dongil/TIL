function solution(s) {
  let answer = 0;
  if (s[0] == '+'){
      s.slice(0, 1)
  }
  answer = parseInt(s)
  return answer;
}