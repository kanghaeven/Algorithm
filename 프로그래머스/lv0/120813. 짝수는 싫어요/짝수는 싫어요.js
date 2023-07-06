function solution(n) {
    var answer = [];
    for (i = 1; i <= n; i++) {
        if (i % 2 === 1) {
            answer.push(i)
        }
    }
    return answer;
}