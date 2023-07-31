function solution(num_list) {
    var answer = [];
    let cnt00 = 0;
    let cnt01 = 0;
    num_list.map(e => {
        if (e % 2 === 0) {
            cnt00 += 1;            
    } else {
        cnt01 += 1;
    }
    });
    answer.push(cnt00);
    answer.push(cnt01);
    console.log(answer);
    return answer;
}