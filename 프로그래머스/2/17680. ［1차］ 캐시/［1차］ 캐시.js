function solution(cacheSize, cities) {
    let totalTime = 0;
    const cacheArray = [];
    
    if (cacheSize === 0) {
        return cities.length * 5;
    }
    
    cities.forEach(city => {
        const cityName = city.toLowerCase();
        const cityIndex = cacheArray.indexOf(cityName);
        if (cityIndex !== -1) {
            totalTime += 1;
            cacheArray.splice(cityIndex, 1);
            // console.log(totalTime, "cahce hit");
        } else {
            totalTime += 5;
            // console.log(totalTime, "cahce miss");
        };
        if (cacheArray.length === cacheSize) {
            cacheArray.shift();
        };
        cacheArray.push(cityName);
        // consle.log(cacheArray);
    })
    return totalTime;
}
// cacheSize 캐시 크기, cities 도시이름 배열
// 캐시 크기가 0이면 바로 return 도시이름 개수 * cache miss
// 캐시 크기만큼 배열에 소문자 처리한 도시를 넣고
// 도시이름을 순회할 때 
// 그 배열에 순회하는 도시이름이 있으면 cache hit
// 그 배열에 순회하는 도시이름이 없으면 cache miss
// 계산하고 배열에 오래된 도시 밀어내고 순회하는 도시 뒤에 넣기