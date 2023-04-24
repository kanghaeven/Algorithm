const fs = require('fs');

// - 기준으로 나누기
let input = fs.readFileSync('/dev/stdin').toString().split('-');
// console.log(input); // ['55', '50+40']

for (i = 0; i < input.length; i++) {
    for (j of input[i]) {
        if (j === '+') { // +로 이어져 있는 부분 다 더하기
            let plus = input[i].split('+');
            // console.log(plus); // ['50', '40']
            for (p in plus) {
                plus[p] = parseInt(plus[p]);
            }
            input[i] = plus.reduce((acc, cur) => acc + cur, 0);
            break;
        }
    // console.log(input[i]); // 90
    // console.log(typeof(input[i])); // 문자열 정수 섞여 있을 수도
    }
}
// console.log(input); // ['55', 90]
for (u in input) {
    input[u] = parseInt(input[u]); // 정수로 변환하여 제자리에 할당
}
const sum = input.reduce((acc, cur) => acc + cur, 0); 
const ans = input[0] - (sum - input[0]); // 첫값 - (나머지 다 더한 값)
console.log(ans);