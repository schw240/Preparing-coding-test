# 이전 작동에 k광년 이동시 k-1, k, k+1 광년만 다시 이동 가능
# 점화식 kn = k(n-1) -1 or k(n-1) or k(n-1) + 1
# x에서 y까지 도달하는데 필요한 최소한의 공간이동 장치 작동횟수
#안정성을 위해 마지막은 무조건 1
import math

T = int(input())


for i in range(T):
    x, y = map(int, input().split())
    distance = int(y - x)
    if distance <= 3:
        print(distance)
    else:
        n = int(math.sqrt(distance))
        if distance == n**2:
            print(2*n - 1)
        elif n**2 < distance <= n**2 + n:
            print(2*n)
        else:
            print(2*n + 1)
