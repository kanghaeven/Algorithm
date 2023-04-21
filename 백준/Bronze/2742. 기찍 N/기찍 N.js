const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();
const n = +input;
let answer = '';
for(i = n ; i > 0 ; i--) {
   answer += `${i}
` 
}
console.log(answer)