function solution(arr) {
    let answer = 0;
    arr.forEach((num) => answer += num);
    
    return answer/arr.length;
}