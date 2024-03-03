function solution(food) {
    let answer = '';
    food.forEach((f, fidx) => {
        if (fidx !== 0) {
            for (let i = 0; i < Math.floor(f/2); i++) {
                answer += fidx
            }
        } 
    })
    const rearr = answer.split("").reverse();
    return answer + "0" + rearr.join("");
}