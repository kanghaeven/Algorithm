function solution(dirs) {
    let answer = 0;
    let di = { 'U': [-1,0], 'D': [1,0], 'R': [0,1], 'L': [0,-1] }; 
    let visited = new Set();
    
    let [x, y] = [5, 5]; // 시작 위치

    dirs.split("").forEach(d => {
        let [nx, ny] = [x + di[d][0], y + di[d][1]];
        // 경계를 벗어나지 않는 경우에만 처리
        if (nx >= 0 && ny >= 0 && nx <= 10 && ny <= 10) {
            // 경로의 unique 표현을 만듭니다. "현재 위치 -> 이동한 위치" 와 "이동한 위치 -> 현재 위치"
            let path = `${x}${y}${nx}${ny}`;
            let reversePath = `${nx}${ny}${x}${y}`;

            // 이 경로를 방문하지 않았으면 추가하고 answer를 증가시킵니다.
            if (!visited.has(path) && !visited.has(reversePath)) {
                visited.add(path);
                visited.add(reversePath);  // 양방향 둘 다 추가
                answer++;
            }
            // 현재 위치를 이동한 위치로 업데이트합니다.
            [x, y] = [nx, ny];
        }
    });
    return answer;
}
