const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n');

// console.log(input)

for (let lines of input) {
    const line = lines.split(' ').map(num => parseInt(num));
    // console.log(line)
    line.sort((a, b) => a - b);
    // console.log(line)
    
    if (line[0] === 0) {
        break;
    }

    if (line[0] ** 2 + line[1] ** 2 === line[2] ** 2) {
        console.log('right');
    } else {
        console.log('wrong');
    }
}

