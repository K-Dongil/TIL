const fs = require('fs');
const inputStr = fs.readFileSync('/dev/stdin').toString().trim().split(' ')

console.log(inputStr[0] === "" ? 0 : inputStr.length);