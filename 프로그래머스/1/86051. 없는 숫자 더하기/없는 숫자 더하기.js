function solution(numbers) {
    let answer = 45;
    numbers.forEach(n => {
        answer -= n;
    })
    return answer;
}