function solution(msg) {
    let answer = [];
    let array = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 65)); // 'A'(65)부터 'Z'(90)까지 초기화
   let stack = []
const result = []
for(let i=0; i<msg.length;i++) {
stack.push(msg[i])
if(array.includes(stack.join(''))) continue;
    array.push(stack.join(''));
    stack.pop();
    const index = array.indexOf(stack.join('')) + 1;
    result.push(index);
    stack = [];
    i--;
}
    const index = array.indexOf(stack.join(''))+ 1;
    result.push(index);
return result
}