function solution(s) {
    var answer = "";
    let arr = s.split(" ");
    arr.map(x => {
        answer += x.charAt(0).toUpperCase() + x.slice(1).toLowerCase() + " ";
    })
    answer = answer.slice(0, -1);
    return answer;
}