function solution(my_string) {
    const aeiou = ['a', 'e', 'i', 'o', 'u'];
    const arr = my_string.split('');
    arr.forEach(e => {
        aeiou.forEach(ee => {
            if (e === ee ) {
                my_string = my_string.replace(e, '');
            }
        })
    })
    return my_string;
}