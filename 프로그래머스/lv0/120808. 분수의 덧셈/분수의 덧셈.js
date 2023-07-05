function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    answer = [((numer1 * denom2) + (numer2 * denom1)), (denom1 * denom2)]
    
    for (i = parseInt(denom1 * denom2); i >= 1; i--) {
        if (answer[0] % i === 0 && answer[1] % i === 0) {
            answer[0] /= i;
            answer[1] /= i;
            break;
        }        
    }

    return answer;
}