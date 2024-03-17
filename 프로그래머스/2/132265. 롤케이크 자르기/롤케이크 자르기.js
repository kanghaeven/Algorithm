function solution(topping) {
    let answer = 0;
    let leftMap = new Map();
    let rightMap = new Map();

    for (let t of topping) {
        rightMap.set(t, (rightMap.get(t) || 0) + 1);
    }

    for (let i = 0; i < topping.length; i++) {
        let current = topping[i];
        leftMap.set(current, (leftMap.get(current) || 0) + 1);
        rightMap.set(current, rightMap.get(current) - 1);

        if (rightMap.get(current) === 0) {
            rightMap.delete(current);
        }

        if (leftMap.size === rightMap.size) {
            answer++;
        }
    }
    
    return answer;
}
