const input = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(Number);

const N = input.shift();

function solution(N, input) {
    const dp = [...Array(11)];
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (let i = 4; i < 11; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }

    for (let j = 0; j < N; j ++) {
        console.log(dp[input[j]]);
    }
}

solution(N, input);