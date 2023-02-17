function solution(x, n) {
    let answer = [...Array(n).keys()].map(key => x*(key+1));
    return answer;
}