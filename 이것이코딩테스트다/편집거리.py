# 두 문자가 같은 경우
# dp[i][j] = dp[i-1][j-1]

# 두 문자가 다른 경우
# 왼쪽 삽입, 위쪽 삭제, 왼쪽 위 교체
# dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

def edit_distance(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같다면 왼쪽 위 수 그대로 대입
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # 문자가 다르다면 3가지 경우 중 최소 값
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

    return dp[n][m]


# print(edit_distance("cat", "cut"))
print(edit_distance("saturday", "sunday"))
