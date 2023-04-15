const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split(' ');


a = parseInt(input[0]);
b = parseInt(input[1]);

console.log(a+b);
console.log(a-b);
console.log(a*b);
// 소수점 없앰
console.log(Math.floor(a/b));
console.log(a%b);