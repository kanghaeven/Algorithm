function solution(s) {
    let num =  [1000000, -1000000];
    s.split(" ").forEach(ee => {
        const e = Number(ee);
        if (num[0] > e) {
            num[0] = e
        }
        if (num[1] < e) {
            num[1] = e
        }
    })
    return num.join(" ");
}