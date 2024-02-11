function solution(numbers, target) {
    let answer = 0;
        
    function getAnswer(cnt, value) {
        if(cnt < numbers.length) {
            getAnswer(cnt + 1, value + numbers[cnt]);
            getAnswer(cnt + 1, value - numbers[cnt]);
        } else {
            if (value === target) {
                answer++;
            }
        }
    }
    
    getAnswer(0, 0);
    
    return answer;
}

