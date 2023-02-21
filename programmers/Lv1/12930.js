function solution(s) {
    let answer = '';
    let changeV = true;

    for (let i=0; i<s.length; i++){
        if (s[i] == ' '){
            answer += ' ';
            changeV = true;
        }
        else if (changeV){
            answer += s[i].toUpperCase();
            changeV = false;
        }else{
            answer += s[i].toLowerCase();
            changeV = true;
        }
    }
    
    return answer;
}