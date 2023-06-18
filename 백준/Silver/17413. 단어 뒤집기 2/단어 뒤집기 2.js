const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('')

let stack = []; // 역순으로 저장할 스택
let queue = []; // 정순으로 저장할 큐
let ans = ''; // 결과를 저장할 변수
let isOpen = false; // '<' 태그가 열려 있는지 여부
let size = input.length + 1; // 입력의 길이

for (let i = 0; i < size; i++) {
  let j = input[i]; // 현재 문자

  if (j === '<') {
    isOpen = true; // '<' 태그가 열려있음을 표시
    if (stack.length > 0) {
      ans += stack.reverse().join(''); // 스택의 내용을 역순으로 결과에 추가
      stack = []; // 스택 초기화
    }
  } else if (j === '>') {
    isOpen = false; // '<' 태그가 닫혔음을 표시
    ans += queue.join('') + j; // 큐의 내용과 '>' 문자를 결과에 추가
    queue = []; // 큐 초기화
    continue;      
  } else if ((j === ' ' && !isOpen) || j === undefined) {
    ans += stack.reverse().join('').trim() + (j === ' ' ? j : ''); // 스택 내용을 역순으로 결과에 추가하고, 공백 여부에 따라 결과에 추가
    stack = []; // 스택 초기화
    continue;
  }

  if (isOpen) {
    queue.push(j); // '<' 태그가 열려있으면 큐에 문자 추가
  } else if (!isOpen) {
    stack.push(j); // '<' 태그가 닫혀있으면 스택에 문자 추가
  }
}
console.log(ans); // 결과 출력
