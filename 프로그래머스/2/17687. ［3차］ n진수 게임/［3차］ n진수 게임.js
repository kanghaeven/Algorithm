function solution(n, t, m, p) {
    let answer = '';
    let number = '';
    for (let tm = 0; tm < t * m; tm++) {
        number += tm.toString(n);
    }
    // console.log(number)
    let idx = 0;
    for (let i = 0; i < t; i++) { // 미리 구할 숫자 개수만큼 출력하자
        for (let j = 1; j <= m; j++) { // 인원만큼 순회
            if (j === p) {
                answer += isNaN(number[idx]) ? number[idx].toUpperCase() : number[idx];
                // console.log("내차례야", number[idx], idx)
            } else {
                idx++;
                // console.log("다른사람", number[idx], idx)
            }
        }
        idx++;
    }
    return answer;
}