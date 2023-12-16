function solution(s) {
    let num = s.split(" ");
    return Math.min(...num) + " " + Math.max(...num);
}