const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);
const inn = input.slice(1, N + 1);
const out = input.slice(N + 1);

let cnt = 0;

for (let i = 0; i < N; i++) {
    let index = out.indexOf(inn[i]);

    for (let j = 0; j < i; j++) {
        if (out.indexOf(inn[j]) > index) {
            cnt++;
            break;
        }
    }
}

console.log(cnt);
