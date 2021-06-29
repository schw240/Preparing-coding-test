N = int(input())

# i번 사람이 돈을 인출하는데 걸리는 시간은 p[i]분
P = list(map(int, input().split(' ')))
P.sort()


res = 0

for i in range(N):
    for j in range(i+1):
        res += P[j]

print(res)
