function solution(n) {
    var answer = 0;
    let newArr = [];
    for (i = 0; i <= n; i++) {
        if (i % 2 === 0) {
            newArr.push(i);    
        }        
    }
    answer = newArr.reduce((a, c) => a + c);
    return answer;
}