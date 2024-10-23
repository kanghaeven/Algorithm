def solution(brown, yellow):
    answer = []
    for ysero in range(1, brown + yellow + 1):
        if yellow % ysero == 0:
            ygaro = yellow // ysero
            sero = ysero + 2
            garo = ygaro + 2

            if brown == (garo * 2 + ysero * 2):
                return [garo, sero]