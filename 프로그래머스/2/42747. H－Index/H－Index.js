function solution(citations) {
    let answer = 0;
    const n = citations.length;

    citations.sort((a, b) => b - a); // 내림차순 정렬

    while (answer < n && citations[answer] > answer) {
        answer++;
    }

    return answer;
}
