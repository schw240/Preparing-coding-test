S1 = input()
S2 = input()

len1 = len(S1)
len2 = len(S2)
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        # 가장 최근에 추가된 글자가 서로 같을 때
        if S1[i-1] == S2[j-1]:
            # 추가되기전의 글자 + 1
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 기존 문자열로 만들 수 있었던 최대값
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])
