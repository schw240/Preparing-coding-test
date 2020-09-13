def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x + 1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)



n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1) # a=수직, b=우상향대각선, c=좌상향대각선의 각각 가능한 칸수만큼

def solve(i):
    global ans
    if i == n:                                        # 퀸을 다 놓았다면
        ans += 1                                      # 경우의 수를 한개 추가
        return                                        # 종료
    for j in range(n):                                # 열을 이동하면서
        if not (a[j] or b[i+j] or c[i-j+n-1]):        # 인덱스의 합과 차가 같다는 것을 이용, 세가지 조건에 부합하지 않는다면
            a[j] = b[i+j] = c[i-j+n-1] = True         # True 표시
            solve(i+1)                                # 다음 퀸을 놓기 위해 재귀.
            a[j] = b[i+j] = c[i-j+n-1] = False        # 초기화

solve(0)
print(ans)