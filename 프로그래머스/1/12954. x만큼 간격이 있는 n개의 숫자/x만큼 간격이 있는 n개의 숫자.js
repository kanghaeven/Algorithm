function solution(x, n) {
    var answer = [];
    let a = 0;
    for (let i = 0; i < n; i++) {
        a += x;
        answer.push(a);        
    } 
    return answer;
}

// x부터 시작해 x씩 증가하는 숫자를 n개 지나는 리스트