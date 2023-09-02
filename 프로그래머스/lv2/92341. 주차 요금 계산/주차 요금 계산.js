function solution(fees, records) { // 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원) // 시각, 차량번호, 내역
    const cars = {};
    
    records.forEach(e => {
        let [time, car, type] = e.split(' '); // 입력 [시각, 차량번호, 내역]
        
        const [hour, minute] = time.split(':');
        
        time = hour * 60 + Number(minute); // 분으로 바꾸기
        
        if (!cars[car]) { // 처음 조회되는 차면
            cars[car] = { time: 0, car }; // { '5961': { time: 0, car: '5961' } }
        }
        
        cars[car].type = type; // { '5961': { time: 0, car: '5961', type: 'IN' } }
        
        if (type === "OUT") {
            cars[car].time += time - cars[car].lastInTime;
            return;
        }
        
         cars[car].lastInTime = time;
    })
    
    return Object.values(cars)
    .sort((a, b) => a.car - b.car) // 차량 번호가 작은 자동차부터 
    .map(v => {
      // 차량이 최종적으로 나가지 않았을 때
      if (v.type == "IN") {
        v.time += 1439 - v.lastInTime;
      }
      
      // 기본시간을 넘지 않았을 때
      if (fees[0] > v.time) {
        return fees[1];
      }
            
      return fees[1] + Math.ceil((v.time - fees[0]) / fees[2]) * fees[3];
    });
}