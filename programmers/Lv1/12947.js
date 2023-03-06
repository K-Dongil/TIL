function solution(x) {
    let plusNum = 0
    for (c of x.toString()){
        plusNum += parseInt(c)
    }
    return x % plusNum ? false : true;
}