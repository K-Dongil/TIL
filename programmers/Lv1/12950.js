function solution(arr1, arr2) {
    arr2.map((inArr, outIdx) => {
        inArr.map((v, inIdx) => {
            arr1[outIdx][inIdx] += v
        })
    })
    
    return arr1;
}