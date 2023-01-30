function solution(arr)
{
    let answer = [];
    let left = -1;
    
    for (let i = 0; i<arr.length; i++){
        if (arr[i] !== left){ // answer.at(-1) 이용하면 효율성에서 탈락한다..
            answer.push(arr[i]);
            left = arr[i];
        }
    }
    
    return answer;
}