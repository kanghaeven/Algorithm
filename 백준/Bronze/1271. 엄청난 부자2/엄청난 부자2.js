const fs = require('fs');

let input = fs.readFileSync('/dev/stdin').toString().split(' ');


const n = BigInt(input[0]);
const m = BigInt(input[1]);


console.log((n / m).toString());
console.log((n % m).toString());