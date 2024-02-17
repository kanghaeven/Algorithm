function solution(priorities, location) {
    let answer = 0;
    const queue = priorities.map((priority, index) => ({ index, priority }));
    console.log(queue)

    while (queue.length > 0) {
        const current = queue.shift();
        if (queue.some(item => item.priority > current.priority)) {
            queue.push(current);
        } else {
            answer++;
            if (current.index === location) {
                return answer;
            }
        }
    }
}
