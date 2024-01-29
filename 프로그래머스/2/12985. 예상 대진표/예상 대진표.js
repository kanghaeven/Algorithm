function solution(n,a,b) {
    let answer = 0;
    const arr = [a, b];
    arr.sort((a, b) => a - b);
    a = arr[0];
    b = arr[1];
    while (a % 2 !== 1 || b % 2 !== 0 || b - a !== 1) {
        answer++;
        a = Math.ceil(a/2);
        b = Math.ceil(b/2);
    };
    return answer + 1;
}