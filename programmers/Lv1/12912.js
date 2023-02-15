function solution(a, b) {
    let answer = 0;
    let leftV = a<=b ? a : b;
    let rangeV = a<=b ? b-a+1 : a-b+1;
    
    for (let i=0; i<rangeV; i++){
        answer += leftV+i;
    }
    
    return answer;
}