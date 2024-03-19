function solution(num) {
    var answer = 0;
    let n = num
    while (n > 0) {
        if (n === 1) break;
        if (n % 2 === 0) {
            n = n / 2;
        } else {
            n = n * 3 + 1;
        }
        answer++;
        if (n === 1) break;
        if (answer === 500) {
            answer = -1;
            break;
        }
    }
    
    return answer;
}