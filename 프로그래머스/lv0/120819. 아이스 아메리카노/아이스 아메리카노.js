function solution(money) {
    var answer = [];
    americano = money / 5500;
    answer.push(Math.floor(americano));
    cash = money % 5500;
    answer.push(cash);
    return answer;
}