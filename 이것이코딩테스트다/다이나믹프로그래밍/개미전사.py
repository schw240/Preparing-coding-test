N = int(input())
arr = list(map(int, input().split(' ')))

# 메뚜기 마을 식량창고가 일직선으로 이어져있는데
# 식량창고를 선택적으로 약탈하여 식량을 빼았는다.
# 인접한 창고를 공격받으면 바로 알아차릴 수 있을 때
# 들키지 않고 식량창고를 약탈하고 식량의 최대값 출력

dp = [0] * 100
dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])  # 이전값 또는 전전값 + 현재값

print(dp[N-1])
