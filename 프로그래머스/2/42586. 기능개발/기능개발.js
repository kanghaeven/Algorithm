function solution(progresses, speeds) {
    var answer = [];
    let stack = [];
    progresses.forEach((p, pidx) => {
        for (let i = 0; i < 100; i++) {
            if (p + speeds[pidx]*i >= 100) {
                stack.push(i);
                break;
            }
        }
    })
    console.log(stack)
    while (stack.length > 0) {
        for (let q = 0; q < stack.length; q++) {
            let a = 1;
            const tmp = stack.shift();
            console.log("ddd", tmp, stack)
            for (let j = 0; j <= stack.length; j++) {
                console.log(j, stack)
                if (tmp >= stack[j]) {
                    a++;
                } else {
                    stack.splice(0, j);
                    break;
                }  
            }
            console.log(stack, tmp, a);
            answer.push(a);
            if (stack.length <= 0) {
                break;
            }
        }  
    }
 
    return answer;
}

// 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
// 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됨

// 각 배포마다 몇 개의 기능이 배포되는지 return
// 배포는 하루에 한번 가능