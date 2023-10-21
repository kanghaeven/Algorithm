function solution(keymap, targets) {
    const keypadOf = [];
    const keypad = [];
    // 자판
    for (let i = 0; i < keymap.length; i++) {
        // 키
        for (let j = 0; j < keymap[i].length; j++) {
            if (keypadOf.indexOf(keymap[i][j]) === -1) {
                keypadOf.push(keymap[i][j]);
                keypad.push([keymap[i][j], j + 1]);
            }
            // 문자마다 최소 인덱스로 바꿈
            for (let q = 0; q < keypad.length; q++) {
                if ((keymap[i][j] === keypad[q][0]) && (j < keypad[q][1])) {
                    keypad[q][1] = j + 1;
                }
            }
        }
    }
    // console.log(keypad);
    
    const ans = [];
    for (let i = 0; i < targets.length; i++) {
        let flag = true;
        let cnt = 0;
        for (let j = 0; j < targets[i].length; j++) {
            let newcnt = cnt;
            for (let q = 0; q < keypad.length; q++) {
                if ((targets[i][j] === keypad[q][0])) {
                    cnt += keypad[q][1];
                }
            }
            if (newcnt === cnt) {
                flag = false;
            }
        }
        // 목표 문자열 작성 불가 시 -1
        if (flag === false) {
            ans.push(-1);
        } else {
            ans.push(cnt);
        }
    }
    
    return ans;
}