function solution(m, n, board) {
    let answer = 0;
    const map = board.map(b => b.split(""));
    
    while (true) {
        let block = [];
        
        for (i = 0; i < m - 1; i++) {
            for (j = 0; j < n - 1 ; j++) {
                if (map[i][j] !== 0 &&
                    map[i][j] === map[i][j+1] && 
                    map[i][j] === map[i+1][j] && 
                    map[i][j] === map[i+1][j+1]) {
                    block.push([i, j]);
                } 
            }
        }
        
        if (block.length === 0) {
            break;
        }
        
        block.forEach(b => {
            let [x, y] = b;
            map[x][y] = 0;
            map[x][y+1] = 0;
            map[x+1][y] = 0;
            map[x+1][y+1] = 0;
        })
        
        // console.log(map)
        
        for (let j = 0; j < n; j++) {
            for (let i = m - 1; i >= 0; i--) {
                if (map[i][j] === 0) {
                    for (let k = i - 1; k >= 0; k--) {
                        if (map[k][j] !== 0) {
                            map[i][j] = map[k][j];
                            map[k][j] = 0;
                            break;
                        }

                    }
                }
            }
        }
    }
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (map[i][j] === 0) {
                answer++;
            }
        }
    }

    return answer;
}