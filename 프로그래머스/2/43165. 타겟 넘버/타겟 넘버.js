function solution(numbers, target) {
    const arr = []
    const makeTarget = (cnt, sum, arr)=>{
        if (numbers.length === cnt) {
            if (sum === target) {
                arr.push(true);
            };
            return;
        };
        makeTarget(cnt + 1, sum + numbers[cnt], arr);
        makeTarget(cnt + 1, sum - numbers[cnt], arr);
        // console.log(cnt, sum, arr)
    };
    makeTarget(0, 0, arr);
    return arr.length;
}

// n개의 음이 아닌 정수들
// 순서 바꾸지 않고 적절히 더하거나 뺴서 타겟넘버 만드는 방법의 수

