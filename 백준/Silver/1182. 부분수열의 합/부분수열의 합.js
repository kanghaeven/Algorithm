const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, S] = input[0].split(" ").map((value) => Number(value));
const list = input[1].split(" ").map((value) => Number(value));
let result = 0;

// 조합 함수 정의
function combination(array, lastIndex) {
  const sum = array.reduce((a, b) => a + b, null); // 배열의 합

  // 부분 수열의 합이 S와 같으면 결과값 증가
  if (sum == S) {
    result++;
  }

  // 배열에서 원소를 하나씩 추가하면서 모든 조합을 찾음
  for (let i = lastIndex; i < N; i++) {
    array.push(list[i]); // 원소 추가
    combination(array, i + 1); // 재귀 호출을 통해 다음 위치의 원소 추가 시도
    array.pop(); // 원소 제거하여 다른 조합을시도
  }
}

combination([], 0);
console.log(result);
