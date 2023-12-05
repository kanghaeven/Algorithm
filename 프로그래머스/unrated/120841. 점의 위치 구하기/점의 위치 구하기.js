function solution(dot) {
    var answer = 0;
    console.log(dot);
    dot.map((e, eidx) => {
        if (eidx === 0) {
            if (e < 0) {
                answer = -1
            } else {
                answer = 1
            }
        }
        if (eidx === 1) {
            if (e < 0) {
                if (answer === -1) {
                    answer = 3
                } else {
                    answer = 4
                }
            } else {
                if (answer === -1) {
                    answer = 2
                } else {
                    answer = 1
                }   
            }
        }
    })
    return answer;
}