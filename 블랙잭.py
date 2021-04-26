N, M = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
cards.sort(reverse=True)

for i in range(N):
    for j in range(i+1, N):
        for k in range(j + 1, N):
            sum_value = cards[i] + cards[j] + cards[k]

            # 최적화
            if res > sum_value:
                break

            if sum_value <= M:
                res = max(res, sum_value)

print(res)
