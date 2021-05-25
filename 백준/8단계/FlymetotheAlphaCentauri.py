# kn = kn-1 -1 or kn-1 or kn-1 + 1

T = int(input())
for i in range(T):
    X, Y = map(int, input().split(' '))
    # X부터 Y까지 도달하는데 필요한 공간이동 장치 횟수
    cnt = 0
    k = 1
    while X != Y:
        X += k
        cnt += 1
        k +=
    print(cnt)
