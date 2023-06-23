const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0].split(' ')[0]);
const m = parseInt(input[0].split(' ')[1]);
const poketmons = input.slice(1, n + 1);
const questions = input.slice(n + 1, n + m + 1);

function solution(poketmons, questions) {
    const map = new Map(poketmons.map((poketmon, index) => [poketmon, index + 1]));
    questions.forEach(question => {
        if (Number.isNaN(parseInt(question))) { // 숫자인지 확인
            console.log(map.get(question)); // question 키로 사용, (index + 1)을 가져옴
        } else {
            console.log(poketmons[question - 1]);
        }
    });
}

solution(poketmons, questions);