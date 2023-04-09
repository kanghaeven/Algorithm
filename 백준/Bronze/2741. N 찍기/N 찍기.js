const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString();

let n = '';

for (let i = 1; i <= input; i++) {
    n += i + '\n'
}

// n이라는 빈 문자열에 담은 후 출력해야 시간초과 해결

console.log(n);