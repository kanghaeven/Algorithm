const fs = require("fs");

const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map((e) => parseInt(e)));

const [n, m] = input.shift();

const bfs = (start) => {
  let queue = [start]; // 탐색 시작 좌표
  let picSize = 1; // 시작 포함 그림 넓이

  visited[start[0]][start[1]] = 1; // 시작 좌표 방문 처리

  while (queue.length > 0) {
    // while (queue) X -> shift할 때 배열이 비어있어도 참으로 간주되어 무한루프
    let [x, y] = queue.shift();

    for (let f = 0; f < 4; f++) {
      const [nx, ny] = [x + di[f][0], y + di[f][1]]; // 사방 탐색
      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        // 범위 설정
        if (input[nx][ny] === 1 && visited[nx][ny] === 0) {
          // 그림있고 미방문 시
          visited[nx][ny] = 1; // 방문 처리
          picSize += 1; // 그림 넓이 +1
          queue.push([nx, ny]); // 계속 돌려
        }
      }
    }
  }
  return picSize;
};

let picCnt = 0; // 그림 수
let maxPicSize = 0; // 최대 그림 넓이

const visited = Array.from(Array(n), () => Array(m).fill(0));

const di = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (input[i][j] === 1 && !visited[i][j]) {
      // 그림있고 미방문 시
      picSize = bfs([i, j]); // 각 지점마다 그림 넓이 구하는 bfs
      picCnt += 1; // 그림 수 +1

      // 최대 그림 넓이 구하기
      if (picSize > maxPicSize) {
        maxPicSize = picSize;
      }
    }
  }
}

console.log(picCnt);
console.log(maxPicSize);
