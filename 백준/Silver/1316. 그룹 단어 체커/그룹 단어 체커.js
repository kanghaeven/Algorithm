const fs = require('fs');
const [n, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let cnt = 0;

input.map(e => {
    const a = e.split('')
    const arr = [];
    let prev = "";
    let flag = false;
    a.map(ee => {
        if (arr.indexOf(ee) === -1 || prev === ee) {
            if(arr.indexOf(ee) === -1 ) {
                arr.push(ee);
            }
            prev = ee;
        } else {
            flag = true;
            return;
        }
    })
    if (flag === false) {
        cnt++;
    }
})

console.log(cnt);