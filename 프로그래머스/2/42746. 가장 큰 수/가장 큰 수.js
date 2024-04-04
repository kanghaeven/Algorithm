function solution(numbers) {
    numbers.sort((a, b) => {
        const aa = a.toString();
        const bb = b.toString();
        if (bb + aa < aa + bb) return -1;
        if (bb + aa > aa + bb) return 1;
        return 0;
    });
    return numbers.reduce((a, b) => a + b, 0) === 0 ? "0" : numbers.join('');
}