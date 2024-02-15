function solution(s) {
    const tuple = [];
    const arr = [];
    s.slice(2, s.length-2).split("},{").map(e => {
        arr.push(e);
    });
    arr.sort((a, b) => a.length - b.length);
    let prev = []
    arr.forEach((a, aidx) => {
        a.split(",").map(t => {
            if (aidx > 0) {
                prev = arr[aidx-1].length > 0 ? arr[aidx-1].split(",").map(Number) : [];
                
            }
            const tmp = parseInt(t);
            if (prev.length > 0) {
                // console.log("여기",tmp, prev.includes(tmp))
                if (prev.includes(tmp) === false) {
                    tuple.push(tmp);
                    // console.log("튜플2", prev, tmp, tuple)
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