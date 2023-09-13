const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input.shift());

const meeting = input.map(e => e.split(' ').map(Number));

// 상담 기간
const T = [0]; // [ 0, 3, 5, 1, 1, 2, 4, 2 ]
// 상담 금액
const P = [0]; // [ 0, 10, 20,  10, 20, 15, 40, 200 ]
// 해당 날에 받을 수 있는 최대 돈
const dp = Array.from({ length: N + 2 }, () => 0); // [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

for (i = 0; i < N; i++) {
  T.push(meeting[i][0]);
  P.push(meeting[i][1]);
}

// 지금 내가 받은 돈
let max = 0;
// 하루 시작할 때 내 지갑에 돈 확인
for (let wallet = 1; wallet < N + 2; wallet++) {
  if (max < dp[wallet]) {
    max = dp[wallet];
  }
  // 돈 받는 날 = 오늘 일자 + 작업 일자
  let day = wallet + T[wallet];
  if (day < N + 2) {
    dp[day] = Math.max(dp[day], max + P[wallet]);
  }
}

console.log(max);