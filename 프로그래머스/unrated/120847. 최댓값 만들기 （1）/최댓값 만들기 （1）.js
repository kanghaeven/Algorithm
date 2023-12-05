function solution(numbers) {
    var answer = 0;
    numbers.forEach((e, eidx) => {
        numbers.forEach((ee, eeidx) => {
            if (answer < e * ee && eidx !== eeidx) {
                answer = e * ee;
            }
        })
    });
    return answer;
}