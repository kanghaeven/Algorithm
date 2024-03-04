function solution(word) {
    let answer = 0;
    let words = ['A', 'E', 'I', 'O', 'U'];
    let tmp = [];

    function DFS(s, depth) {
        if (depth <= 5) {
            tmp.push(s);
            for (let i = 0; i < words.length; i++) {
                DFS(s + words[i], depth + 1);    
            }
        }
    }

    DFS('', 0);
    answer = tmp.indexOf(word);

    return answer;
}