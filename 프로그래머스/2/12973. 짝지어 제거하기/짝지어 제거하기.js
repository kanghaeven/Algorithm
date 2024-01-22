function solution(s) {
    const stack = [];
    for (let i of s) {
        stack.push(i);
        if (stack[stack.length - 1] === stack[stack.length - 2]) {
            stack.pop();
            stack.pop();
        };
    };
    const answer = stack.length === 0 ? 1 : 0;
    return answer;
}

// 같은 알파벳 2개 붙어있는 짝 제거, 문자 이어붙이기
// 모두 제거했다면 1
// 아니면 0