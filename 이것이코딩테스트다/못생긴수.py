# 2, 3, 5만을 소인수로 가지는 수
# 2, 3, 5를 약수로 가지는 합성수
# n 번째 못생긴 수

n = int(input())
dp = [0] * 20
ugly = [1]
# 1은 못생긴 수
dp[0] = 1

# 2,3,5 인덱스
i2 = i3 = i5 = 0
# 처음 곱셈값들
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(next2, next3, next5)

    # 2, 3, 5의 배수?
    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[n-1])
# for i in range(1, 20):
#     if i % 2 == 0:
#         dp[i] = i
#     if i % 3 == 0:
#         dp[i] = i
#     if i % 5 == 0:
#         dp[i] = i


# print(dp)
