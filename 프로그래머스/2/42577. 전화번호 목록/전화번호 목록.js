function solution(phone_book) {
    let answer = true;
    const hashMap = {};

    // 해시맵에 전화번호를 키로 저장
    for (const number of phone_book) {
        hashMap[number] = true;
    }

    // 전화번호 목록을 순회하면서 접두사가 있는지 확인
    for (const number of phone_book) {
        if (!answer) break;
        let prefix = "";
        for (const digit of number) {
            prefix += digit;
            // 해시맵에서 현재 전화번호의 접두사를 검색
            if (hashMap[prefix] && prefix !== number) {
                answer = false;
                break;
            }
        }
    }
    return answer;
}
