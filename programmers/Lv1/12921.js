function solution(n) {
    let answer = n;
    let visited = new Array(n+1).fill(false);
    
    for (let i = 2; i<n+1; i++){
        if (visited[i] === false){
            for (let j = 2; j<(n+1)/i; j++){
                visited[i*j] = true;
            }
        }
    }
    
    return visited.filter((n)=> n=== false).length -2;
}