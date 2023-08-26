const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const T = parseInt(input.shift());

const di = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

const dfs = (x, y, field) => {
  field[x][y] = 0; // 이 배추는 확인 완료

  for (let f = 0; f < 4; f++) {
    // 인접 배추 확인
    const [nx, ny] = [x + di[f][0], y + di[f][1]];
    if (
      0 <= nx &&
      nx < field.length &&
      0 <= ny &&
      ny < field[0].length &&
      field[nx][ny] === 1
    ) {
      // 범위 안에 있고 배추 있으면
      dfs(nx, ny, field); // 해당 인접 배추 재귀 호출
    }
  }
  return;
};

for (let t = 0; t < T; t++) {
  const [M, N, K] = input.shift().split(" ").map(Number); // 가로, 세로, 배추 위치 개수

  const field = Array.from({ length: N }, () => Array(M).fill(0)); // 땅

  for (let k = 0; k < K; k++) {
    const [i, j] = input.shift().split(" ").map(Number); // 배추 위치
    field[j][i] = 1; // 배추 위치 따라 심기
  }

  let ans = 0;

  for (let n = 0; n < N; n++) {
    for (let m = 0; m < M; m++) {
      if (field[n][m] === 1) {
        dfs(n, m, field);
        ans++; // 배추가 서로 인접한 구역 개수 === 필요한 지렁이 최소 개수
      }
    }
  }

  console.log(ans);
}
