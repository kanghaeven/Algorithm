const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input.shift().split(" ").map(Number);

const maze = input.map((el) => el.split("").map(Number));

const di = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

let ans = 0;
let visited = Array.from(Array(n), () => Array(m).fill(0));

const bfs = (start) => {
  const queue = [start];
  visited[start[0]][start[1]] = 1; // 시작 위치 경로 길이 1

  while (queue.length > 0) {
    const [x, y] = queue.shift();

    // 현재 위치가 도착점이면 탐색 종료
    if (x === n - 1 && y === m - 1) {
      ans = visited[x][y];
      return ans; // 도착점의 방문 길이
    }

    for (let f = 0; f < 4; f++) {
      const [nx, ny] = [x + di[f][0], y + di[f][1]];
      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if (maze[nx][ny] === 1 && !visited[nx][ny]) {
          visited[nx][ny] = visited[x][y] + 1; // 각 위치까지의 경로 길이 visited에 저장
          queue.push([nx, ny]);
        }
      }
    }
  }
};

console.log(bfs([0, 0]));
