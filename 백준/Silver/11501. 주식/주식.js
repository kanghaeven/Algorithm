const fs = require("fs");

const [T, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const ans = [];

for (let i = 0; i < parseInt(T); i++) {
  const N = parseInt(input.shift());
  const arr = input.shift().split(" ").map(Number);

  let maxPrice = arr[N - 1];
  let profit = 0;

  for (let j = N - 2; j >= 0; j--) {
    if (arr[j] < maxPrice) {
      profit += maxPrice - arr[j];
    } else {
      maxPrice = arr[j];
    }
  }

  ans.push(profit);
}

console.log(ans.join("\n"));