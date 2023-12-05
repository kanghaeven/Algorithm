function solution(array, height) {
    var answer = 0;
    console.log(array, height);
    array.map(e => {
        if (e > height) {
            answer++;
        }
    })
    return answer;
}