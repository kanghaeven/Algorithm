const fs = require('fs');

const [T, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split("\n").map(Number);

input.forEach(i => {
  let a = "";
  if (i === 1) {
    a = 0;
  } else if (i % 2 === 0) {
    for (let ii = 0; ii < i; ii++) {
      a += 1;
    }
  } else {
    a += 1;
    for (let ii = 0; ii < i-2; ii++) {
      a += 2;
    }
    a += 1;
  }
  console.log(a);
})