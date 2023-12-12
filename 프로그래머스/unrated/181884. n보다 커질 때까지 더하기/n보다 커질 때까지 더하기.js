function solution(numbers, n) {
    var answer = 0;
    numbers.forEach(e => {
        if (answer <= n) {
            answer += e;;
        }
    })
    return answer;
}