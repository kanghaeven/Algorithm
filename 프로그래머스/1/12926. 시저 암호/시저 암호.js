function solution(s, n) {
    var answer = '';
    const A = Array(26).fill().map((v, i) => String.fromCharCode(i + 65));
    const a = Array(26).fill().map((v, i) => String.fromCharCode(i + 97));
    s.split("").forEach(s => {
        if (s !== " ") {
            let tmp = 0;
            if (A.indexOf(s) !== -1) {
                tmp = A.indexOf(s) + n;
                answer += A[tmp % 26];
            } else {
                tmp = a.indexOf(s) + n;
                answer += a[tmp % 26];
            }    
        } else {
            answer += s;
        }
    })
    return answer;
}