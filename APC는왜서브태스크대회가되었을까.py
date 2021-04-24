import sys
input = sys.stdin.readline

# 현정이 역량 L, K개 문제 해결 가능
N, L, K = map(int, input().split())

# 쉬운 문제는 100점, 어려운문제는 140점
# L보다 작거나 같은 난이도의 문제 해결 가능
# K개보다 많은 문제는 해결 X
# 어려운 버전을 해결하면 쉬운버전도 같이 풀림
score = 0
problem = list()
for i in range(N):
    sub1, sub2 = map(int, input().split())
    problem.append([sub1, sub2])

for i in range(K):
    if problem[i][0] <= L and problem[i][1] <= L:
        score += 140
    elif problem[i][0] <= L and problem[i][1] > L:
        score += 100


print(score)
