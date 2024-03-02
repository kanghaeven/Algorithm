function solution(x) {
    let answer = true;
    const s = x.toString().split("").reduce((acc, cur) => acc + parseInt(cur), 0);
    if (x % s !== 0) answer = false;
    return answer;
}