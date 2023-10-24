const input = require("fs")
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split("\n");

const [rows, cols, totalSeconds] = input[0].split(" ").map(Number);
const grid = Array.from({ length: rows }, () => Array(cols).fill(null));
const bombTimers = Array.from({ length: rows }, () => Array(cols).fill(0));
const directions = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];
let currentSecond = 1;

for (let i = 1; i <= rows; i++) {
  const row = input[i].split("");
  for (let j = 0; j < cols; j++) {
    grid[i - 1][j] = row[j];
    if (row[j] === "O") bombTimers[i - 1][j] = 3;
  }
}

while (currentSecond <= totalSeconds) {
  if (currentSecond % 2 === 0) {
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (grid[i][j] === ".") {
          grid[i][j] = "O";
          bombTimers[i][j] = currentSecond + 3;
        }
      }
    }
  } else {
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (bombTimers[i][j] === currentSecond) {
          grid[i][j] = ".";

          for (let k = 0; k < 4; k++) {
            const nextRow = i + directions[k][0];
            const nextCol = j + directions[k][1];

            if (nextRow < 0 || nextCol < 0 || nextRow >= rows || nextCol >= cols) continue;

            if (grid[nextRow][nextCol] === "O" && bombTimers[nextRow][nextCol] !== currentSecond) {
              grid[nextRow][nextCol] = ".";
              bombTimers[nextRow][nextCol] = 0;
            }
          }
        }
      }
    }
  }

  currentSecond += 1;
}

let result = "";
for (let i = 0; i < rows; i++) {
  result += grid[i].join("");
  result += "\n";
}

console.log(result);