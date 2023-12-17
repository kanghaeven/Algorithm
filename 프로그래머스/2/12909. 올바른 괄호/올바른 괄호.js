function solution(s){
    let answer = true;
    const arr = [];
    let cnt = 0;
    s.split("").forEach((e, eidx) => {
        if (e === "(") {
            cnt++;
        }
        if (e === ")") {
            if (eidx === 0) {
                answer = false;
            }
            cnt--;
            if (cnt < 0) {
                answer = false;
            }
        }
        arr.push(e);
    })
    if (cnt !== 0 || arr[arr.length - 1] === "(") {
        answer = false;
    }
    return answer;
}