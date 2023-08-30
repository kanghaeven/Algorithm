const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input.shift());

const location = Array.from(Array(N), () => new Array()); // 지도
// 배열을 가리키는 포인터(참조)로서 고정되어 있지만, 배열 내부의 요소는 여전히 수정 가능 => const
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    location[i].push(input[i][j]);
  }
}

const di = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

const dfs = (x, y) => {
  location[x][y] = "0"; // 중복 방문 방지 위해 방문 처리
  let villageCnt = 1; // 각 단지내 집 수
  for (let f = 0; f < 4; f++) {
    [nx, ny] = [x + di[f][0], y + di[f][1]];
    if (0 <= nx && nx < N && 0 <= ny && ny < N && location[nx][ny] === "1") {
      villageCnt += dfs(nx, ny);
    }
  }
  return villageCnt;
};

let cnt = 0; // 총 단지 수
let villageCntArr = []; // 각 단지내 집 수 저장
for (let x = 0; x < N; x++) {
  for (let y = 0; y < N; y++) {
    if (location[x][y] === "1") {
      cnt++;
      villageCntArr.push(dfs(x, y));
    }
  }
}

console.log(cnt);
villageCntArr.sort((a, b) => a - b); // 오름차순 정렬
console.log(villageCntArr.join("\n"));
