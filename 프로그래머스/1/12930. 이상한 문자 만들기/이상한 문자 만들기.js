function solution(s) {
    let answer = '';
    s.split(" ").forEach((ss, ssidx) => {
        ss.split("").forEach((sss, sssidx) => {
            if (sssidx % 2 === 0) {
                answer += sss.toUpperCase();
                // console.log(sss)
            } else {
                answer += sss.toLowerCase();
            }
        })
        if (ssidx !== s.split(" ").length - 1) {
            answer += ' ';
        }
    })
    return answer;
}