function solution(my_string, letter) {
    var answer = '';
    const a = [...my_string];
    const filterArr = a.filter(function(strlet) {
        return strlet !== letter;
    });
    answer = filterArr.join('');

    return answer;
}