const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let answer = 0;
const di = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]];

function solution(i, j, w, h, island) {
  if (island[i][j] !== 1) return; // 바다거나 이미 방문한 곳이면 리턴

  island[i][j] = -1; // 방문
  for (let d = 0; d < 8; d++) {
    const [x, y] = [i + di[d][0], j + di[d][1]];
    if (0 <= x && x < h && 0 <= y && y < w) {
      solution(x, y, w, h, island); // 주변 탐색
    }
  }
}

while (input.length > 0) {
  const [w, h] = input.shift().split(' ').map(Number);
  if (w === 0 && h === 0) break;
  
  const island = [];
  for (let l = 0; l < h; l++) {
    island.push(input.shift().split(' ').map(Number));
  }

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (island[i][j] === 1) {
        solution(i, j, w, h, island);
        answer++;
      }
    }
  }
  console.log(answer);
  answer = 0; // 다음 섬을 계산하기 위해 초기화
}
