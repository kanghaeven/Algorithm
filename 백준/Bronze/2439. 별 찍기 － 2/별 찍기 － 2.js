const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString();

let star = "";
let blank = "";

for (i = 1; i <= input; i++) {
    star += "*";
    for (j = 0; j < input - i; j++) {
        blank += " ";
    }
    console.log(blank + star);
    blank = "";
}
