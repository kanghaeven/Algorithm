function solution(k, dungeons) {
    let answer = 0;
    let visited = Array(dungeons.length).fill(false);

    function DFS(k, count) {
        for (let i = 0; i < dungeons.length; i++) {
            if (k >= dungeons[i][0] && !visited[i]) {
                visited[i] = true;
                DFS(k - dungeons[i][1], count + 1);
                visited[i] = false; 
            }
        }
        answer = Math.max(answer, count);
    }

    DFS(k, 0);

    return answer;
}

// 최소 필요 피로도 : 각 던전마다 탐험을 시작하기 위해 가지고 있어야됨
// 소모 피로도 : 던전 탐험을 마쳤을 때 소모됨