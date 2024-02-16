function solution(progresses, speeds) {
    let answer = [];
    let stack = [];
    
    progresses.forEach((p, pidx) => {
        for (let i = 0; i < 100; i++) {
            if (p + speeds[pidx]*i >= 100) {
                stack.push(i);
                break;
            }
        }
    })

    while (stack.length > 0) {
        for (let q = 0; q < stack.length; q++) {
            let a = 1;
            const tmp = stack.shift();
            for (let j = 0; j <= stack.length; j++) {
                if (tmp >= stack[j]) {
                    a++;
                } else {
                    stack.splice(0, j);
                    break;
                }  
            }
            answer.push(a);
            if (stack.length <= 0) {
                break;
            }
        }  
    }
 
    return answer;
}
