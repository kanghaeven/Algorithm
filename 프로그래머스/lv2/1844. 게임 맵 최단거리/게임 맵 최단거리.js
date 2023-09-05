function solution(maps) {
    let ans = 0;
    const di = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let cnt = 0;
    const bfs = () => {
        const queue = [[0, 0]];
        const distance = Array.from({ length: maps.length }, () => Array(maps[0].length).fill(0));
        distance[0][0] = 1
        cnt++;
        
        while (queue.length > 0) {
            const [x, y] = queue.shift();

            for (f = 0; f < 4; f++) {
                const [nx, ny] = [x + di[f][0], y + di[f][1]];
                if (0 <= nx && nx < maps.length && 0 <= ny && ny < maps[0].length && maps[nx][ny] === 1 && distance[nx][ny] === 0) {
                    distance[nx][ny] = distance[x][y] + 1; // 이동할 수 있는 위치의 값을 거리로 업데이트
                    // console.log(distance)
                    queue.push([nx, ny]);
                }
            }
        }
        return distance[maps.length - 1][maps[0].length - 1] || -1; // 도착 지점까지 도달할 수 없으면 -1 반환
    }
    return(bfs());
    
}