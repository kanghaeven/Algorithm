function solution(numbers) {
    let hap = 0;
    numbers.map(e => hap += e);
    return hap/numbers.length;
}