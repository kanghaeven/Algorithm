function solution(my_string) {
    var answer = '';
    const a = my_string.split('');
    a.reverse();
    answer = a.join('');
    return answer;
}