function solution(s) {
    const middleNum =s.length/2;
    const answer = middleNum == parseInt(middleNum) ? s[middleNum-1]+s[middleNum] : s[parseInt(middleNum)];
    return answer;
}