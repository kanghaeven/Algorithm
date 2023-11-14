const fs = require('fs');
const [N, K] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

const arr = [];

for (let i = 1; i <= N; i++) {
  arr.push(i);
}

const ans = [];

let idx = 0;
while (arr.length > 0) {
  idx = (idx + K - 1) % arr.length;
  ans.push(arr.splice(idx, 1)[0]);
}

console.log(`<${ans.join(', ')}>`);