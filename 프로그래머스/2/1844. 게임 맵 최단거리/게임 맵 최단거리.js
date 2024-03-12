function solution(maps) {
    const di = [[-1,0], [0,1], [1,0], [0,-1]];
    
    function bfs() {
        const queue = [[0, 0]];
        const route = Array.from({length: maps.length}, () => Array(maps[0].length).fill(0));
        route[0][0] = 1;
        
        while (queue.length > 0) {
            const [x, y] = queue.shift();
            
            for (let i = 0; i < 4; i++) {
                const [nx, ny] = [x + di[i][0], y + di[i][1]];
                if (0 <= nx && 0 <= ny && nx < maps.length && ny < maps[0].length 
                    && maps[nx][ny] === 1 && route[nx][ny] === 0) {
                    route[nx][ny] = route[x][y] + 1;
                    queue.push([nx, ny]);
                }
            }
        }
        // console.log(route)
        return route[maps.length - 1][maps[0].length - 1] || -1;
    }
    return bfs();
}
