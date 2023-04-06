const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString();

let star = "";

// for (초기식; 조건식; 증감식) {
// 실행문;
// }
for (let i = 0; i < input; i++) {
    star += "*"
    console.log(star);
}
// i++ 변수 i 증가, 자기자신 i++ 바로 증가되지 않음
// ++i 변수 i 증가, 자기자신 i++ 바로 증가됨