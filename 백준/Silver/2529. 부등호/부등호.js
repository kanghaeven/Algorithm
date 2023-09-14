const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(input[0]);

const inequality = input[1].split(' ');

const ans = []; 

function solution(str, cnt) {
  if (cnt === N + 1) { // 만약 모든 부등호를 사용했으면
    ans.push(str); // 조건을 만족하는 숫자 조합을 배열에 추가
    return;
  } else {
    const last = parseInt(str[cnt - 1]); // 이전 숫자를 가져옴 (cnt는 1부터 시작하므로 cnt-1)
    if (inequality[cnt - 1] === '>') { // 부등호가 '>'인 경우
      for (let i = 0; i < 10; i++) {
        if (!str.includes(`${i}`) && last > i) { // 아직 사용되지 않은 숫자이고, 이전 숫자보다 작은 경우
          solution(str + `${i}`, cnt + 1); // 재귀 호출
        }
      }
    } else { // 부등호가 '<'인 경우
      for (let i = 0; i < 10; i++) {
        if (!str.includes(`${i}`) && last < i) { // 아직 사용되지 않은 숫자이고, 이전 숫자보다 큰 경우
          solution(str + `${i}`, cnt + 1); // 재귀 호출
        }
      }
    }
  }
}

for (let i = 0; i < 10; i++) {
  solution(`${i}`, 1);
}

const minNumber = ans.shift(); 
const maxNumber = ans.pop();  

console.log(maxNumber + '\n' + minNumber);
