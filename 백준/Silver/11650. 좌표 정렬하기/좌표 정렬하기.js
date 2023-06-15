const [n, ...coords] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

console.log(
    coords
    .map((v => ([parseInt(v.split(' ')[0]), parseInt(v.split(' ')[1])])))
    .sort((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    })
    .map(v => String(v[0]) + " " + String(v[1])).join('\n')
);