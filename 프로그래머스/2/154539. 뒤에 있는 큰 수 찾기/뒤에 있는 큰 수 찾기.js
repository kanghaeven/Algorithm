function solution(numbers) {
    // 스택 사용: 스택에는 인덱스를 저장합니다.
    const stack = [];
    
    // 모든 원소의 결과를 -1로 초기화합니다.
    const answer = new Array(numbers.length).fill(-1);
    
    // numbers의 각 원소에 대하여...
    numbers.forEach((number, i) => {
        // 스택이 비어있지 않고, 현재 숫자가 스택의 최상단에 있는 숫자보다 크면
        while (stack.length > 0 && numbers[stack[stack.length - 1]] < number) {
            // 스택에서 인덱스를 pop하고, 해당 인덱스의 값을 현재 숫자로 업데이트합니다.
            answer[stack.pop()] = number;
        }
        // 현재 인덱스를 스택에 push합니다.
        stack.push(i);
    });
    
    // 남아있는 스택에 대하여 이미 -1로 초기화되어 있으므로 별도 처리가 필요 없습니다.
    return answer;
}
