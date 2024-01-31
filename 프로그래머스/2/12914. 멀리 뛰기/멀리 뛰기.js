function solution(n) {
    let answer = Array(n + 1).fill(0);
    
    answer[1] = 1;
    answer[2] = 2;
    
    for (let i = 3; i <= n; i++) {
        answer[i] = (answer[i - 1] + answer[i - 2]) % 1234567;
    };
    
    return answer[n];
}

// 한번에 1칸 or 2칸
// 몇 가지 % 1234567
// if (n === 3) answer = (x-1) * 2 - 1 = 4 - 1 = 3;
// if (n === 4) answer = (x-1) * 2 - 2 = 6 - 1 = 5;
// if (n === 5) answer = (x-1) * 2 - 2 = 10 - 2 = 8;