N = int(input())
A = list(map(int, input().split(' ')))


increase = [1] * (N + 1)
decrease = [1] * (N + 1)

for i in range(N):
    for j in range(i):
        # 증가만 하는 경우
        if A[j] < A[i]:
            increase[i] = max(increase[i], increase[j] + 1)


for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

res = [0] * (N + 1)
for i in range(N):
    res[i] = increase[i] + decrease[i] - 1

print(max(res))
