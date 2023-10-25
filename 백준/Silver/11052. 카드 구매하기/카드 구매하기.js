const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = parseInt(input[0]);
const prices = input[1].split(' ').map(Number);

const dp = Array(n + 1).fill(0);

for (let i = 1; i <= n; i++) {
  for (let j = 1; j <= i; j++) {
    dp[i] = Math.max(dp[i], dp[i - j] + prices[j - 1]);
  }
}

console.log(dp[n]);