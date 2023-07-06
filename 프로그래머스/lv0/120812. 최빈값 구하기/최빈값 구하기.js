function solution(array) {
    var answer = 0;
    let newArray = new Array(Math.max(...array) + 1).fill(0);
    
    for (let i = 0; i < array.length; i++) {
        newArray[array[i]] += 1;
    }
    
    if (newArray.indexOf(Math.max(...newArray)) !== newArray.lastIndexOf(Math.max(...newArray))) {
        answer = -1;
    } else {
        answer = newArray.indexOf(Math.max(...newArray));
    }
    
    console.log(answer)
    return answer;
}