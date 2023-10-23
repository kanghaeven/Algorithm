const fs = require('fs');

const [N, input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const arr = input.split(' ').map(Number);

const dp = Array(parseInt(N)).fill(1);

for (let i = 1; i < parseInt(N); i++) {
  for (let j = 0; j < i; j++) {
    if (arr[i] > arr[j]) {
      dp[i] = Math.max(dp[i], dp[j] + 1);
    }
  }
}

console.log(Math.max(...dp));