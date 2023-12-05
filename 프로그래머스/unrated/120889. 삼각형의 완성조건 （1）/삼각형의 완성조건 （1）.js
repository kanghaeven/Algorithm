function solution(sides) {
    var answer = 0;
    var maxSide = Math.max(...sides); // 가장 긴 변 찾기
    var sumOfOtherTwo = 0;

    // 가장 긴 변을 제외한 나머지 두 변의 길이의 합 계산
    for (var i = 0; i < sides.length; i++) {
        if (i !== sides.indexOf(maxSide)) {
            sumOfOtherTwo += sides[i];
        }
    }

    // 가장 긴 변의 길이가 나머지 두 변의 길이의 합보다 작으면 삼각형 가능
    if (maxSide < sumOfOtherTwo) {
        answer = 1;
    } else {
        answer = 2;
    }

    return answer;
}
