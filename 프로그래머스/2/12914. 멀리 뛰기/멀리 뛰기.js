function solution(n) {
    let answer = Array(n + 1).fill(0);
    
    answer[1] = 1;
    answer[2] = 2;
    
    for (let i = 3; i <= n; i++) {
        answer[i] = (answer[i - 1] * 2 - (answer[i - 1] - answer[i - 2])) % 1234567;
        console.log(i, answer[i - 1] * 2 , Math.floor(i / 2), answer[i]);
    };
    
    return answer[n] % 1234567;
}

// 한번에 1칸 or 2칸
// 몇 가지 % 1234567
// if (n === 3) answer = (x-1) * 2 - 1 = 4 - 1 = 3;
// if (n === 4) answer = (x-1) * 2 - 2 = 6 - 1 = 5;
// if (n === 5) answer = (x-1) * 2 - 2 = 10 - 2 = 8;
// if (n === 6) answer = (x-1) * 2 - 3 = 16 - 3 = 13;
// if (n === 7) answer = (x-1) * 2 - 3 = 26 - 3 = 13;