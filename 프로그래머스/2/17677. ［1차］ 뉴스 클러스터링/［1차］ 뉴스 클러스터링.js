function solution(str1, str2) {
    let answer = 0;
    let reg = /[^a-zA-Z]/gim;
    const str = [[str1, []], [str2, []]];
    str.forEach(s => {
        s[0].split("").forEach((e, eidx) => {
            if (eidx !== s[0].length - 1) {
                const t = e + s[0][eidx + 1];
                const tmp = t.replace(reg, "").toUpperCase();
                if (tmp.length === 2) {
                    s[1].push(tmp);
                }
            }
        })
    })
    console.log(str[0][1], str[1][1]);
    
    const arr = [[], []]
    str[0][1].forEach(e => {
        if (str[1][1].indexOf(e) !== -1) {
            const idx = str[1][1].indexOf(e);
            str[1][1].splice(idx, 1);
            arr[0].push(e);
        } else {
            arr[1].push(e);
        }
        // console.log(str[1][1], arr[0], arr[1])
    })

    const hap = [...arr[0], ...arr[1], ...str[1][1]];
    // console.log(arr[0]);
    // console.log(hap);
    
    if (arr[0].length === 0 && hap.length === 0) {
        answer = 1;
    } else {
        answer = arr[0].length / hap.length;
    }
    
    return Math.floor(answer * 65536);
}

// 두글자씩 끊었을 때 교 / 합 * 65536 소수점 버림