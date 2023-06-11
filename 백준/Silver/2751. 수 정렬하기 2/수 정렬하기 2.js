const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number);

const num = []

for (i = 1; i < input[0] + 1; i++) {
    num.push(input[i])
}

const setnum = num.sort((a, b) => a - b);

console.log(setnum.join('\n'));
