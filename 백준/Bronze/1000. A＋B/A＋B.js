// 파일 읽어오기 위해 Node.js의 built-in file system module fs 사용
const fs = require('fs');

// input 읽어와 변수로 선언 및 할당
// 그 내용을 input에 저장, toString(), split() 사용
// Array로 저장됨
// // 백준에서는 'input.txt'를  '/dev/stdin'으로 변경
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

// input에서 지정한 값을 읽어와 다른 변수로 선언 및 활용
// toString메소드로 지금은 문자열이기 때문에 paseInt로 숫자로 형태 변환
const a = parseInt(input[0]);
const b = parseInt(input[1]);

console.log(a + b)
