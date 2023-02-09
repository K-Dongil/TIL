function solution(s) {
    let answer = !s.match(/[a-zA-Z]/g) && (s.length == 4 || s.length == 6) ? true : false;
    return answer;
}