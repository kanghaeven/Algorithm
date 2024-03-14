function solution(land) {
    const dp = Array.from({length : land.length}, () => Array(4).fill(0));

    dp[0] = land[0];
    for (let i = 0; i< land.length - 1; i++){
        for (let j = 0; j < 4; j++)
            for (let k = 0; k < 4; k++){
                if (j===k) continue;
                const temp = dp[i][j] + land[i+1][k];
                if(temp > dp[i+1][k]) dp[i+1][k] = temp;
                // console.log(dp, dp[i][j], land[i+1][k])
            }
    }

    return Math.max(...dp[land.length - 1]);
}