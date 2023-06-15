const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = input.shift();

const num = input.map(ele =>
    ele.split(' ').map(nums => parseInt(nums)))

let ans = '';

num
    .sort((prev, cur) => {
        if (prev[0] !== cur[0]) {
            return prev[0] - cur[0];
        }
        return prev[1] - cur[1];
    })
    .forEach(ele => {
        ans += `${ele[0]} ${ele[1]}\n`
    })

console.log(ans)