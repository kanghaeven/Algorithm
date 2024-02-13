function solution(clothes) {
    var answer = 0;
    
    const obj = {};
    clothes.forEach(c => {
        if (obj[c[1]] === undefined) {
            obj[c[1]] = [c[0]]
            console.log(obj)
        } else {
            obj[c[1]].push(c[0])
            console.log(obj)
        }
    })
    
    const f = Object.keys(obj);

    answer = 1;
    
    f.forEach(ff => {
        answer *= (obj[ff].length + 1);
    })

    // for (let [key, value] of Object.entries(obj)) {
    //     answer *= (obj[key].length + 1);
    //     console.log(key, value, answer)
    // }

    answer -= 1;
    

    return answer;
}

// 각 종류별로 1가지만
// 다른 의상이 겹치지 않거나, 추가 착용 시 다른 방법으로 착용한거임
// 최소 한 개의 의상 착용

// 1종류 3     = 3   
// 2종류 2,1   = 5   2^2 + 2^1 :6 - 1 = 5
// 3종류 1,1,1 = 7   3^1 + 3^1 + 3^1 :9 - 2 = 7
// 3종류 2,2,2 = 26  3^2 + 3^2 + 3^2 :27 -  = 26
// 3종류 3,3,3 = 63  3^3 + 3^3 + 3^3 :81 - 18 = 63

// 1종류 3     = 3   1*3 = 3   
// 2종류 2,1   = 5   2*2 * 2*1 :8  -  2^1 + 1^1 :3 = 5
// 3종류 1,1,1 = 7   3*1 * 3*1 * 3*1 :27  -  3^1 :20 = 7
// 3종류 2,2,2 = 26  3^2 + 3^2 + 3^2 :27 -  = 26
// 3종류 3,3,3 = 63  3^3 + 3^3 + 3^3 :81 - 18 = 63

