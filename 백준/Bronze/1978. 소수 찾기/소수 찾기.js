const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const number = input[1].split(' ').map(Number);

function isPrime(n) {
    if (n < 2) return false; // 0과 1은 소수가 아님

    for (let i = 2; i <= Math.sqrt(n); i++ ) { // 제곱근까지만 확인
        if (n % i === 0) {
            return false; // 약수가 존재하면 소수가 아님
        }
    }

    return true; // 약수 존재하지 않으면 소수
}

let cnt = 0;

for (let num of number) {
    if (isPrime(num)) {
        cnt++;
    }
}

console.log(cnt)