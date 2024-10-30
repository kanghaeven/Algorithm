def solution(k, dungeons):
    def dfs(k, dungeons, visited, cnt, maxcnt):
        maxcnt[0] = max(maxcnt[0], cnt)
        for i in range(len(dungeons)):
            if visited[i] == 0 and k >= dungeons[i][0]:
                visited[i] = 1
                dfs(k - dungeons[i][1], dungeons, visited, cnt + 1, maxcnt)
                visited[i] = 0
        return maxcnt
    
    maxcnt = [0]
    visited = [0 for _ in range(len(dungeons))]
    return dfs(k, dungeons, visited, 0, maxcnt)[0]