function solution(n) {
    var answer = 0;
    const nBinOne = n.toString(2).replaceAll("0", "").length;
    for (i = n + 1; i <= 1000000; i++) {
        if (i.toString(2).replaceAll("0", "").length === nBinOne) {
            return i;    
        }       
    }
}

// n의 다음 큰 숫자는 n보다 큰 자연수
// n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같음
// n의 다음 큰 숫자는 조건 1, 2를 만족하는 가장 작은 수