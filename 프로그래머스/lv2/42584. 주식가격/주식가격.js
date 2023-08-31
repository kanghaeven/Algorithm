function solution(prices) {
    var answer = [];
    const N = prices.length;
    
    for (i = 0; i < N; i++) {
        let cnt = 0;
        // let tmp = 0;
        for (j = i + 1; j < N; j++) {
            if (prices[i] <= prices[j]) {
                cnt++;
            } else if (prices[i] > prices[j]) {
                cnt++;
                break;
            }
            // if (tmp > prices[j]) {
            //     break;
            // }
            // tmp = prices[j];
        }
        answer.push(cnt);
    }
    return answer;
}