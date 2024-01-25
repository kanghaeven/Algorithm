function solution(n) {
    let ans = 0;
    
    while (n !== 0) {
        if (n % 2 === 0) {
            n = n / 2;
        } else {
            n--;
            ans++;
        }
    }
    
    return ans;
}

// K칸을 앞으로 점프 -> K만큼 건전지 줄음
// 현재까지 온 거리 * 2의 위치로 순간이동 -> 건전지 줄지X
// 최소 건전지 사용량