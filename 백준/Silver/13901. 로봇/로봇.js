const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [R, C] = input.shift().split(" ").map(Number); // 방 크기 세로 R, 가로 C

const room = [];

for (r = 0; r < R; r++) {
  room.push(Array(C).fill(0));
}

const k = input.shift(); // 장애물 개수

for (i = 0; i < k; i++) {
  const [br, bc] = input.shift().split(" ").map(Number);
  room[br][bc] = -1; // 장애물 위치 -1
}

let [sr, sc] = input.shift().split(" ").map(Number); // 로봇 시작 위치

const direction = input
  .shift()
  .split(" ")
  .map((e) => parseInt(e) - 1); // 이동 방향 1위, 2아래, 3왼, 4오

const di = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
]; // 이동 방향 좌표 0, 1위, 2아, 3왼, 4오

let nowDi = 0;
let flag = false;
let end = true;

while (end) {
  room[sr][sc] = 1; // 방문 처리
  flag = false;
  // console.log(room);
  for (f = 0; f < 4; f++) {
    const [nx, ny] = [
      sr + di[direction[nowDi]][0],
      sc + di[direction[nowDi]][1],
    ]; // 움직일 좌표
    if (0 <= nx && nx < R && 0 <= ny && ny < C) {
      // 만약 움질일 좌표가 벽이 아니고
      if (room[nx][ny] === 0) {
        // 미방문 이면
        [sr, sc] = [nx, ny]; // 다음 좌표 설정
        flag = true;
        break;
      }
    }
    nowDi = (nowDi + 1) % 4;
  }
  if (flag === false) {
    end = false;
  }
}
console.log(sr, sc);

// 00  -10 00
// 0-1  00 01
// 00   10 00
