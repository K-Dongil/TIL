function solution(num) {
    let answer = 0;
    
    while (num != 1 & answer < 501){
        num % 2 ? num = 3*num+1 : num /= 2;
        answer += 1;
    }
    
    return answer <= 500 ? answer : -1;
}