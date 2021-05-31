# 2, 3, 5만을 소인수로 가지는 수
# 2, 3, 5를 약수로 가지는 합성수
# n 번째 못생긴 수

# Ugly 수가 맞는지 확인하기
# 1. 2로 더이상 나눌 수 없을 때 까지 나누고 몫 리턴
# 2. 1의 결과값에 대해 3으로 더이상 나눌 수 없을 때 까지 나누고 몫 리턴
# 3. 2의 결과값에 대해 5로 더이상 나눌 수 없을 때 까지 나누고 몫을 리턴
# 4. 3의 결과값이 1이라면 Ugly Number


# def max_div(num1, num2):
#     while num1 % num2 == 0:
#         num1 //= num2
#     return num1

# def isUgly(num):
#     num_div2 = max_div(num, 2)
#     num_div3 = max_div(num_div2, 3)
#     res = max_div(num_div3, 5)

#     if res == 1:
#         return True
#     else:
#         return False

def get_ugly_number(N):
    dp = [0] * N
    dp[0] = 1

    idx_ugly2 = idx_ugly3 = idx_ugly5 = 0

    next_ugly2 = 2
    next_ugly3 = 3
    next_ugly5 = 5

    # 1 - 2 - 3 - 5 - ...

    # ugly num은 2,3,5만 갖는 수들의 수열
    # 각 ugly num 수열의 값에 * 2 한 수
    # 각 ugly num 수열의 값에 * 3 한 수
    # 각 ugly num 수열의 값에 * 5 한 수

    # 위 3개 수열중 최소값을 찾아 dp에 추가
    # dp에 값을 추가시킨 수열은 다음 값을 현재 값으로 갱신
    # 다시 수열 비교 후 dp 추가 - > 해당 수열 값 갱신

    for i in range(1, N):
        # 최소값 dp 추가
        dp[i] = min(next_ugly2, next_ugly3, next_ugly5)
        # dp에 값을 추가 시킨 수열은 다음 값을 현재 값으로 갱신
        if dp[i] == next_ugly2:
            idx_ugly2 += 1
            next_ugly2 = dp[idx_ugly2] * 2
        if dp[i] == next_ugly3:
            idx_ugly3 += 1
            next_ugly3 = dp[idx_ugly3] * 3
        if dp[i] == next_ugly5:
            idx_ugly5 += 1
            next_ugly5 = dp[idx_ugly5] * 5

    return dp[-1]


N = int(input())
print(get_ugly_number(N))
