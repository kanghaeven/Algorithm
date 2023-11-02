const fs = require('fs');
const [n, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = parseInt(n);

const arr = Array();

input.map((e) => {
    arr.push(e.split(' ').map(Number))})

const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

function bfs(x, y, h, visited) {
    const queue = [[x, y]];
    visited[x][y] = true;

    while (queue.length > 0) {
        const [cx, cy] = queue.shift();

        for (let i = 0; i < 4; i++) {
            const nx = cx + dx[i];
            const ny = cy + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny] && arr[nx][ny] > h) {
                visited[nx][ny] = true;
                queue.push([nx, ny]);
            }
        }
    }
}

let result = 0;

for (let i = 0; i <= 100; i++) {
    const visited = Array.from({ length: N }, () => Array(N).fill(false));
    let count = 0;
    for (let j = 0; j < N; j++) {
        for (let k = 0; k < N; k++) {
            if (!visited[j][k] && arr[j][k] > i) {
                bfs(j, k, i, visited);
                count++;
            }
        }
    }
    result = Math.max(result, count);
}

console.log(result);