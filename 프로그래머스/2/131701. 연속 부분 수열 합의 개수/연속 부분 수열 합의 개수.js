function solution(elements) {
    var answer = [];
    const circle = [...elements, ...elements];
    
    circle.forEach((e, eidx) => {
        if (eidx < elements.length) {
            for (let i = 0; i < circle.length; i++) {
            const arr = circle.slice(i, i + eidx + 1);
            answer.push(arr.reduce((acc, cal) => acc + cal, 0));
            // console.log(arr, answer);
            }
        }
    })
    
    const set = new Set(answer);
    // console.log(set, [...set].length);  
    return [...set].length;
}

// 원형 수열 : 처음과 끝이 연결된 일반 수열
// 연속 부분 수열의 합으로 만들 수 있는 수의 개수