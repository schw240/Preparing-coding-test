# N이 1이 될때까지
# 1. N에서 1을 뺌
# 2. N이 K로 나누어 떨어질때만 N을 K로 나눈다.

N, K = map(int, input().split())

cnt = 0
while(N > 1):
    if(N % K == 0):
        N = N // K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)
