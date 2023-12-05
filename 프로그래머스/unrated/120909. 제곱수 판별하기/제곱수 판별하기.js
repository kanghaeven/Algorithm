function solution(n) {
    var answer = 2;

    if (Math.sqrt(n) % 1 === 0) {
        answer = 1;
    };
    return answer;
}