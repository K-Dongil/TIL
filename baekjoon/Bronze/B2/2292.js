const fs = require("fs");  
let input = +fs.readFileSync("/dev/stdin").toString();  

function solution(N) {  
    N;  
    let temp = 1;  
    let cnt = 1;
    
    while (true) {  
        if (N <= temp) {  
            break;  
        }  
        temp = temp + cnt * 6;    
        cnt++;  
    }  
    console.log(cnt);  
}

solution(input);  