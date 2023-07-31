function solution(n, k) {
    var answer = 0;
    const sale = Math.floor(parseInt(n / 10))
    answer = n * 12000 + k * 2000 - sale * 2000
    return answer;
}