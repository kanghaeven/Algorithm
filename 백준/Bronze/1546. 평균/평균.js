const input = require('fs').readFileSync('/dev/stdin').toString().split('\n')

const n = input.shift()
const num = input.shift().split(' ')

const score = num.map(ele => ele / Math.max(...num) * 100);

const hap = score.reduce((acc, cur) => {return acc + cur});

console.log(hap / n);

