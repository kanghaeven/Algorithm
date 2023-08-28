class MinHeap { // 최소힙
    constructor() { // 클래스 인스턴스 생성할 때 초기화 작업
        this.heap = []; // 배열로 힙 구현
    }
    
    size() { // 내부에서 정의한 데이터 구조의 크기 반환
        return this.heap.length; // 힙의 크기 반환
    }
    
    peek() { // 내부에서 정의한 데이터 구조에서 가장 첫 번째 값 가져옴
        return this.heap[0]; // 힙의 가장 작은 값 반환
    }
    
    push(value) {
        this.heap.push(value); // 새 값을 힙에 추가
        let idx = this.heap.length - 1; // 새로 추가한 값의 인덱스
        
        // 부모와 비교하며 힙 속성 유지
        while (idx > 0) {
            const parentIdx = Math.floor((idx - 1) / 2); // 부모 인덱스 계산
            if (this.heap[parentIdx] <= this.heap[idx]) {
                // 부모가 더 작거나 같으면 힙 속성 만족하므로 종료
                break;
            }
            // 부모와 자식 위치 바꿈
            [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
            idx = parentIdx; // 다음 부모 노드로 이동
        }
    }
    
    pop() {
        const heapSize = this.heap.length;
        if (heapSize === 0) {
            return null; // 힙 비어있으면 null 반환
        }
        
        const minValue = this.heap[0]; // 가장 작은 값 저장
        this.heap[0] = this.heap[heapSize - 1]; // 가장 마지막 값 루트로 옮김
        this.heap.pop(); // 마지막 값 삭제
        
        let idx = 0; // 현재 루트 노드의 인덱스
        while (true) {
            const leftChildIdx = idx * 2 + 1; // 왼쪽 자식의 인덱스
            const rightChildIdx = idx * 2 + 2; // 오른쪽 자식의 인덱스
            let minIdx = idx; // 현재 노드를 가장 작은 값으로 가정
            
            if (leftChildIdx < heapSize && this.heap[leftChildIdx] < this.heap[minIdx]) {
                // 왼쪽 자식이 현재 값보다 작으면 인덱스를 갱신
                minIdx = leftChildIdx;
            }
            if (rightChildIdx < heapSize && this.heap[rightChildIdx] < this.heap[minIdx]) {
                // 오른쪽 자식이 현재 값보다 작으면 인덱스를 갱신
                minIdx = rightChildIdx;
            }
            
            if (minIdx === idx) {
                break; // 자식들보다 작거나 같으면 힙 속성 만족하므로 종료
            }
            
            // 현재 노드와 가장 작은 자식을 교환
            [this.heap[idx], this.heap[minIdx]] = [this.heap[minIdx], this.heap[idx]];
            idx = minIdx; // 다음 노드로 이동
        }
        
        return minValue; // 가장 작은 값을 반환
    }
}

function solution(scoville, K) {
    let answer = 0; // 섞은 횟수
    
    const minHeap = new MinHeap();
    scoville.forEach(item => minHeap.push(item)); // 스코빌 지수 힙에 넣음
    
    while (minHeap.size() >= 2 && minHeap.peek() < K) {
        // 힙의 크기가 2 이상이고 가장 작은 값이 K보다 작은 동안 반복
        const low1 = minHeap.pop(); // 가장 작은 값 꺼냄
        const low2 = minHeap.pop(); // 그 다음으로 작은 값 꺼냄
        const mixedScoville = low1 + low2 * 2; // 두 값을 섞은 스코빌 지수 계산
        minHeap.push(mixedScoville); // 섞은 값 다시 힙에 넣음
        answer++; // 섞은 횟수 증가
    }
    // 힙에서 가장 작은 값이 K보다 작다면 모든 음식을 섞을 수 없는 경우이므로 -1 반환
    return minHeap.peek() < K ? -1 : answer;
}
