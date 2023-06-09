const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n');


for (word of input) {
    if (word == 0) break;
    
    let flag = true;
    const palindrome = [...word].reverse();

    for (i in palindrome) {
        if ([...word][i] !== palindrome[i]) {
            flag = false;
            if (flag === false) break;
        }
    }

    if (flag === true) {
        console.log('yes');
    } else {
        console.log('no');
    }
}