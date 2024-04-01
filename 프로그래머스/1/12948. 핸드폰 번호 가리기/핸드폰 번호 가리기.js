function solution(phone_number) {
    let answer = '';
    phone_number.split('').reverse().forEach((n, nidx) => {
        if (nidx < 4) answer += n;
        else answer += '*';
    })
    return answer.split('').reverse().join('');
}