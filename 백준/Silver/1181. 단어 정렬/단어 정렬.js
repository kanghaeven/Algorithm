const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(input[0]);

const words = [];

for (let i = 1; i < N+1; i++) {
    words.push(input[i]);
}

const setwords = [...new Set(words)];

setwords.sort((a, b) => a.length - b.length || a.localeCompare(b));

console.log(setwords.join('\n'));
