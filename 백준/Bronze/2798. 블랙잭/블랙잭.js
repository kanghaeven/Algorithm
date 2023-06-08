const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const nm = input[0].split(' ').map(Number);

const N = nm[0]; // 카드 개수
const M = nm[1]; // 이하 가까운 수

const number = input[1].split(' ').map(Number); // 카드

let ans = 0;

for (let i = 0; i < N; i++) {
    for (let j = i + 1; j < N; j++) {
        for (let l = j + 1; l < N; l++) {
            let sum = number[i] + number[j] + number[l];
            if (sum > ans && sum <= M) { // 기존 값보다 크고 M 이하
                ans = sum;
            }
        }
    } 
}

console.log(ans)