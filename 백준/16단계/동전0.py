N, K = map(int, input().split(' '))

A = []
for i in range(N):
    A.append(int(input()))

num = 0

for i in range(N-1, -1, -1):
    if K == 0:
        break
    if A[i] > K:
        continue
    num += K // A[i]
    K = K % A[i]

print(num)
