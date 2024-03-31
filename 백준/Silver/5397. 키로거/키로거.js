const fs = require('fs');

const [t, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

input.forEach(i => {
  const arr1 = [];
  const arr2 = [];
  i.split('').forEach(ii => {
    if (ii === '<') {
      if (arr1.length > 0) arr2.push(arr1.pop());
    } else if (ii === '>') {
      if (arr2.length > 0) arr1.push(arr2.pop());
    } else if (ii === '-') {
      arr1.pop();
    } else {
      arr1.push(ii);
    }
  })
  console.log(arr1.join('') + arr2.reverse().join(''));
})