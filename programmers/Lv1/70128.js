function solution(a, b) { // a, b 배열의 내적 구하기
    let answer = 0;
    listLength = a.length
    
    for (let i = 0; i < listLength; i++){
        answer += a[i] * b[i]
    }
    
    return answer;
}