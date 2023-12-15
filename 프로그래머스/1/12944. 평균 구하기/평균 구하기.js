function solution(arr) {
    const total = arr.reduce((acc, cur) => acc + cur, 0);
    const answer = total / arr.length;
    return answer;
}