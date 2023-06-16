let [ N,...input ] = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(v => v.split(" "));

const queue = [];
let ans = '';
for(let i = 0; i < N; i++) {
    //
    switch(input[i][0]){
        case "push":
            queue.push(input[i][1]);
            break;
        case "pop":
            ans += (queue.length === 0 ? "-1" : queue.shift()) + "\n";
            break;
        case "size":
            ans += (queue.length) + "\n";
            break;
        case "empty":
            ans += (queue.length === 0 ? "1" : "0") + "\n";
            break;
        case "front":
            ans += (queue.length === 0 ? "-1" : queue[0]) + "\n"; 
            break;
        case "back":
            ans += (queue.length === 0 ? "-1" : queue[queue.length - 1]) + "\n";
            break;
    };    
};
console.log(ans);