const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const A = BigInt(input[0]);
const B = BigInt(input[1]);

console.log(`${A+B}\n${A-B}\n${A*B}`);
