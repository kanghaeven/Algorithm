const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const tall = input[1].split(' ').map(Number);

const line = new Array(N).fill(0);

for (let i = 0; i < N; i++) {
  let cnt = tall[i];
  for (let j = 0; j < N; j++) {
    if (cnt === 0 && line[j] === 0) {
      line[j] = i + 1;
      break;
    }
    if (line[j] === 0) {
      cnt--;
    }
  }
}

console.log(line.join(' '));