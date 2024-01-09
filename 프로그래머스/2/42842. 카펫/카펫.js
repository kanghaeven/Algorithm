function solution(brown, yellow) {
    for (let i = 1; i<= yellow; i++) { // i yellow 세로
        if (!Number.isInteger(yellow / i)) { // 정수로 나누어지지않으면 continue
            continue;
        }
        const j = yellow / i // yellow 가로
        const row = j + 2 // 카펫 가로
        const col = i + 2 // 카펫 세로
        if (brown === row * 2 + i * 2) {
            return [row, col];
        }
    }
}

// [카펫 가로 row, 카펫 세로 col]
// 가로 >= 세로
// 노란색 : 중앙
// 갈색 : 테두리
