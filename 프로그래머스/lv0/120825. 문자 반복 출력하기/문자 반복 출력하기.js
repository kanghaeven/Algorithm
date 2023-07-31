function solution(my_string, n) {
    var answer = '';
    const hello = [...my_string];
    for (let i = 0; i < hello.length; i++) {
        for (let j = 0; j < n; j++) {
            answer += hello[i]; 
        }
    }
    return answer;
}