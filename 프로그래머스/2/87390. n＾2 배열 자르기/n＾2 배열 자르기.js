function solution(n, left, right) {
  let arr = [];
  for (let i = left; i <= right; i++) {
    arr.push(Math.max(Math.floor(i/n) + 1, i%n + 1));
  }
  return arr;
}

// max(1,1)max(1,2)max(1,3) = 1 2 3
// max(2,1)max(2,2)max(2,3) = 2 2 3
// max(3,1)max(3,2)max(3,3) = 3 3 3

// 012 345 678
// 123 223 333

// idx / n = 2 / 3 = 0 + 1 = 1
// idx % n = 2 % 3 = 1 + 1 = 2