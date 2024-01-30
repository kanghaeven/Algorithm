function solution(arr) {
    arr.sort((a, b) => b - a);
    let answer = 0;
    let isDivide = false;
    whileCnt = arr[0];
    
    while (!isDivide) {
        isDivide = arr.every((e) => whileCnt % e === 0);
        if (isDivide){
            answer = whileCnt;
            break;
        }
        whileCnt++;
    }
    return answer;
}
