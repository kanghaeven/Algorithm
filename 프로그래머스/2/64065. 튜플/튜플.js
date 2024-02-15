function solution(s) {    
    const arr = [];
    s.slice(2, s.length-2).split("},{").map(e => {
        arr.push(e);
    });
    arr.sort((a, b) => a.length - b.length);
    
    const tuple = [];
    let prev = [];
    arr.forEach((a, aidx) => {
        a.split(",").map(t => {
            if (aidx > 0) {
                prev = arr[aidx-1].length > 0 ? arr[aidx-1].split(",").map(Number) : [];
            };
            const tmp = parseInt(t);
            if (prev.length > 0) {
                if (prev.includes(tmp) === false) {
                    tuple.push(tmp);
                }
            } else {
                tuple.push(tmp);
                // console.log("튜플", tmp, tuple)
            }
            
    
            // console.log(a, prev)
        })
    })
    return tuple;
}