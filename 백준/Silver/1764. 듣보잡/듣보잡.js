const [NM, ...name]= require('fs').readFileSync('/dev/stdin').toString().split('\n');
// 듣도 못한 사람 수, 보도 못한 사람 수, 명단
const [N, M] = NM.split(' ');

const listen = new Set();
const watch = new Set();
const answer = [];

for (let i = 0; i < N; i++) {
    listen.add(name[i]);
}

for (let j = N; j < parseInt(N) + parseInt(M); j++) {
    watch.add(name[j]);
}

listen.forEach((item) => {
    if (watch.has(item)) {
        answer.push(item);
    }
});

answer.sort();

console.log(answer.length);
console.log(answer.join('\n'));
