T = int(input())


def mining(n, m, golds):
    # 3, 4
    dp = []
    idx = 0
    # map = [[0 for _ in range(m)] for _ in range(n)]
    # for i in range(n):
    #         map[i][j] = []
    for i in range(n):
        dp.append(golds[idx:idx+m])
        idx += m

    # print(dp)
    # m번에 걸쳐서 오른쪽 위, 오른쪽, 오른쪽 아래 3가지중 이동 가능
    # 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램
    # 1열 아무행에서
    # 왼쪽 아래, 왼쪽, 왼쪽 위중 최대값을 더해주기
    for j in range(1, m):
        # 행마다 확인
        # 예외처리.. 범위 확인
        for i in range(n):
            # 위에서 못옴
            if i == 0:
                # 왼쪽에서 오는거랑 왼쪽 아래에서 오는거
                dp[i][j] = max(dp[i][j-1] + dp[i][j],
                               dp[i+1][j-1] + dp[i][j])
            # 아래에서 못옴
            elif i == n-1:
                # 왼쪽에서 오는거랑 왼쪽 위에서 오는거
                dp[i][j] = max(dp[i-1][j-1] + dp[i][j],
                               dp[i][j-1] + dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j-1] + dp[i][j], dp[i]
                                 [j-1] + dp[i][j], dp[i+1][j-1] + dp[i][j])
    result = 0
    for p in dp:
        result = max(result, max(p))

    # print(dp)

    return result


for i in range(T):
    n, m = map(int, input().split(' '))
    golds = list(map(int, input().split(' ')))
    ans = mining(n, m, golds)
    print(ans)
