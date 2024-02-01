function solution(k, tangerine) {
    let answer = 0;

    const dic = {};
    tangerine.forEach(e => {
        if (dic[e] === undefined) dic[e] = 0;        
        dic[e]++;
    });
    
    const entries = Object.entries(dic); 
    // [ [ '1', 1 ], [ '2', 2 ], [ '3', 2 ], [ '4', 1 ], [ '5', 2 ] ]
    console.log(entries);
    
    entries.sort((a, b) => b[1] - a[1]);
    // [ [ '2', 2 ], [ '3', 2 ], [ '5', 2 ], [ '1', 1 ], [ '4', 1 ] ]
    console.log(entries);
    
    while (k > 0) {
        answer++;
        k -= entries.shift()[1];
    }
    
    return answer;
}

// k개 골라 하나의 상자에 담자
// 크기별로 분류
// 크기가 서로 다른 종류의 수의 최솟값