function solution(arr1, arr2) {
    var answer = [];
    
    for (let i = 0; i < arr1.length; i++) {
        const arr = []
        for (let j = 0; j < arr2[0].length; j++) {
            let tmp = 0;
            for (let n = 0; n < arr1[i].length; n++) {
                tmp += arr1[i][n] * arr2[n][j];
            }
            arr.push(tmp);
        }
        answer.push(arr);
    }
    return answer;
}

// C[i][j] = A[i][1]B[1][j] + A[i][2]B[2][j] + ... + A[i][n]*B[n][j]
