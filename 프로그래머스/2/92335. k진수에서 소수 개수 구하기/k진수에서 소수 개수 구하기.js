function solution(n, k) {
    let answer = 0;
    let num = n.toString(k);
    num = num.split("0").map(Number);
    let flag = true;
    for (let i = 0; i < num.length; i++) {
        if (num[i] === 1 | num[i] === 0) continue;
        for (let j = 2; j <= Math.sqrt(num[i]); j++) {
            if (num[i] % j === 0) {
                flag = false;
                break;
            }
        }
        if (flag === false) continue;
        answer++;
    }
    return answer;
}

