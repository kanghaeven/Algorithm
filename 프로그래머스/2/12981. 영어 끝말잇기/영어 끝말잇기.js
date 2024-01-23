function solution(n, words) {
    let answer = [];
    let last = "";
    let now = 0;
    const arr = [];
    
    for (let i of words) {
        now++;
        if (arr.includes(i) || last !== i[0] && arr.length !== 0) {
            answer.push(now % n === 0 ? n : now % n);
            answer.push(Math.ceil(now / n));
            break;
        } else {
            arr.push(i);
            last = i[i.length - 1];
        };
        if (now === words.length && answer.length === 0) {
          answer = [0, 0];
        }
    }
    return answer;
}
// 1번부터 번호 순서대로 단어 말함
// 마지막 사람이 단어를 말한 다음에는 다시 1번
// 앞사람이 말한 단어의 마지막 문자로 시작
// 이전 단어 사용 불가
//
// 가장 먼저 탈락하는 사람 번호, 자신의 몇번째 차례에 탈락하는지