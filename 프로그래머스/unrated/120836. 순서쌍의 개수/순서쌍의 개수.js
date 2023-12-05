function solution(n) {
    var answer = 0;
    for (e = 0; e < n; e++) {
        if (n % e === 0) {
            answer++;
        }
    }
    return answer + 1;
}