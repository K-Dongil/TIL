function solution(n) {
    let answer = 0;
    let idx = 1;
    while (true) {
        let remainder = n % idx;
        if (remainder == 1){
            answer = idx;
            break;
        }
        idx += 1;
    }
    return answer;
}