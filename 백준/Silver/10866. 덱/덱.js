const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const N = input[0];
let deque = [];
let ans = '';

for (let i = 1; i <= N; i++) {
    if (input[i].split(' ').length === 1) {
        if (input[i] === 'size') {
            ans += deque.length + '\n';
        } else if (input[i] === 'empty') {
            if (deque.length === 0) {
                ans += '1\n';
            } else {
                ans += '0\n';
            }
        } else if (input[i] === 'front') {
            if (deque.length === 0) {
                ans += '-1\n';
            } else {
                ans += deque[0] + '\n';
            }
        } else if (input[i] === 'back') {
            if (deque.length === 0) {
                ans += '-1\n';
            } else {
                ans += deque[deque.length - 1] +'\n';
            }
        } else if (input[i] === 'pop_front') {
            if (deque.length === 0) {
                ans += '-1\n';
            } else {
                ans += deque.shift() + '\n';
            }
        } else if (input[i] === 'pop_back') {
            if (deque.length === 0) {
                ans += '-1\n';
            } else {
                ans += deque.pop() + '\n';
            }
        }
    } else {
        if (input[i].split(' ')[0] === 'push_front') {
            deque.unshift(input[i].split(' ')[1]);
        } else {
            deque.push(input[i].split(' ')[1]);
        }
    }
}
console.log(ans);