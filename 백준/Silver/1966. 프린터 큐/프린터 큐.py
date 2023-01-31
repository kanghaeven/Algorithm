import sys
input = sys.stdin.readline
n = int(input())

for testcase in range(n):

    # 문서의 총 개수 n
    # 몇 번째로 뽑히는지 알고 싶은 문서의 현재 인덱스 m
    n, m = map(int,input().split())

    # 문서들의 중요도 que
    que = list(map(int,input().split()))

    # m이 que를 몇 번째에 뽑혔는지 카운트
    cnt = 0

    # m이 -1이 아니라면 아직 뽑히지 않음
    while m != -1:

        # 큐의 맨 앞이 제일 크면 (중요도가 높은 순서대로 뽑히니)
        if que[0] == max(que):
            del que[0] # 삭제
            m -= 1 # m이 한 칸 앞으로
            cnt += 1 # 카운트

        # 큐의 맨 앞이 제일 크지 않으면
        else:
            que.append(que[0]) # 뒤에 추가
            del que[0] # 맨 앞 삭제

            # while문 돌리기 위해 m 변수 조정(남아 있는 큐 중 다른 최대값이 있는 경우니)
            if m == 0: # m이 0이면
                m = len(que) - 1 # 해당자리에 있던 수가 뒤로 갔으니 m도 맨 뒤를 가리킴
            else: # m이 0이 아니면
                m -= 1 # 한 칸 앞 가리킴

    print(cnt)
