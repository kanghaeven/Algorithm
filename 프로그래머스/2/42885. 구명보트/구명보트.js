function solution(people, limit) {
    var answer = 0;
    const arr = people.sort((a, b) => b - a);
    let i = 0;
    let j = arr.length - 1;
    
    while (j >= i) {
        if (arr[i] + arr[j] <= limit) {
            i++;
            j--;
        } else {
            i++;
        }
        answer++;
    } 
    return answer;
}
