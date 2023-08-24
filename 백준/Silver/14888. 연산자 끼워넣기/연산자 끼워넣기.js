const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);
const A = input[1].split(" ").map(Number);
const operators = input[2].split(" ").map(Number); // 연산자 개수 배열

// 사칙연산 함수들을 배열로 선언
const calculate = [
  (a, b) => a + b,
  (a, b) => a - b,
  (a, b) => a * b,
  (a, b) => ~~(a / b),
];

let max = -Infinity;
let min = Infinity;

const dfs = (count = 0, result = A[0]) => {
  if (count === N - 1) {
    // 모든 수를 사용한 경우
    max = Math.max(max, result);
    min = Math.min(min, result);
  } else {
    for (let i = 0; i < 4; i++) {
      // 각 연산자에 대해 순회
      if (!operators[i]) {
        // 해당 연산자가 남아있지 않으면 건너뜀
        continue;
      }
      operators[i]--; // 해당 연산자 사용 표시
      dfs(count + 1, calculate[i](result, A[count + 1])); // 다음 숫자와 연산을 수행하여 재귀 호출
      operators[i]++; // 재귀 호출 후 연산자 사용 표시 해제
    }
  }
};

dfs();
console.log(max);
console.log(min);
