function solution(bridge_length, weight, truck_weights) {
    let answer = 0;
    let bridge = [];
    let currentWeight = 0;
    let time = 0;

    while (truck_weights.length > 0 || bridge.length > 0) {
        answer++;

        if (bridge.length > 0 && bridge[0].end === answer) {
            const truck = bridge.shift();
            currentWeight -= truck.weight;
        }

        if (truck_weights.length > 0 && currentWeight + truck_weights[0] <= weight) {
            const truck = truck_weights.shift();
            bridge.push({ weight: truck, end: answer + bridge_length });
            currentWeight += truck;
        }

        // 다음 트럭이 못 올라오는 상황이면 큐의 첫번째 트럭이 빠지도록 그 시간으로 점프
        if (truck_weights.length > 0 && currentWeight + truck_weights[0] > weight) {
            time = bridge[0].end - 1;
            answer = time;
        }
    }

    return answer;
}
