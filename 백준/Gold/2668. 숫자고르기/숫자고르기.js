const fs = require("fs");

const [N, ...input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n").map(Number);

const nums = [0, ...input];
const answer = [];
let visited = [];

function DFS(start, next) {
  if (visited[next] === 0) {
    visited[next] = 1;
    return DFS(start, nums[next]);
  } else {
    if (start === next) return true;
    return false;
  }
} 

for (let i = 1; i <= N; i++) {
  visited = Array(N + 1).fill(0);
  if (DFS(i, i)) answer.push(i);
}

console.log([answer.length, ...answer].join("\n"));