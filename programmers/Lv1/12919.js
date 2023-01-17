function solution(seoul) {
    let answer = '김서방은 ';
    for (let i = 0; i < seoul.length; i++){
        if (seoul[i] == 'Kim'){
            answer += (i) + '에 있다';
            break;
        }
    }
    return answer;
}