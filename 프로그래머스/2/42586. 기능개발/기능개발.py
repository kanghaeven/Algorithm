def solution(progresses, speeds):
    ans = []
    time = []
    
    # 각 작업이 완료되는데 걸리는 시간 계산
    for i in range(len(progresses)):
        days = -((progresses[i] - 100) // speeds[i])
        time.append(days)
    
    # 배포 가능한 기능 수 계산
    max_days = time[0]
    count = 1
    for i in range(1, len(time)):
        if time[i] <= max_days:
            count += 1
        else:
            ans.append(count)
            count = 1
            max_days = time[i]
    
    # 마지막 배포 추가
    ans.append(count)
    
    return ans