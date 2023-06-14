const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input.shift());

const stack = [];
const ans = [];

for (let i = 0; i < n; i++) {
    switch(input[i]) {
        case 'pop':
            ans.push(stack.pop() || -1);
            break;
        
        case 'size':
            ans.push(stack.length);
            break;
        
        case 'empty':
            ans.push(stack[0] ? 0 : 1);
            break;
        
        case 'top':
            ans.push(stack[stack.length - 1] || -1);
            break;

        default:
            stack.push(input[i].split(" ")[1]);
            break;
    }
}

console.log(ans.join('\n'));