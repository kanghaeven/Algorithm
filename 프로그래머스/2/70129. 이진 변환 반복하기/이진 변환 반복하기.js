function solution(s) {
    let transCnt = 0;
    let zeroCnt = 0;
    while (s.length > 1) {
        const sidx = s.indexOf("0");
        if (sidx !== -1) {
            s = s.substring(0, sidx) + s.substring(sidx + 1);
            zeroCnt++;
        }
        if (!s.includes("0")) {
            const sNum = s.length;
            s = sNum.toString(2);
            transCnt++;
        }
    }
    return [transCnt, zeroCnt];
}