function solution(n) {
    let answer = 0;
    const dp = Array(n + 1).fill(0);
    dp[1] = 1;
    dp[2] = 2;
    for (let i = 3; i <= n; i++) {
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007;    
    }
    return dp[n];
}

// 1 = 1 
// 2 = 2
// 3 = 3  
// 4 = 5  
// 5 = 8  
// 6 = 13 
// 7 = 21 
// 8 = 34
// 9 = 55
// 10 = 59
// 11 = 144
// 12 = 233
// 52 = 316290802