# N개의 수, N-1개의 연산자
# 수 사이에 연산자를 끼워넣어 만들수있는 최대의 결과

N = int(input())
nums = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈 갯수
add, sub, mul, div = map(int, input().split())

# 첫재줄 식의 최대값, 둘째줄 최소값
minV, maxV = 1e9, -1e9


def dfs(i, res, add, sub, mul, div):
    global minV, maxV

    if i == N:
        maxV = max(res, maxV)
        minV = min(res, minV)
        return

    else:
        if add:
            #print(i, res, add, sub, mul, div, "add입니다.")
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            #print(i, res, add, sub, mul, div, "sub입니다.")
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            #print(i, res, add, sub, mul, div, "mul입니다.")
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            #print(i, res, add, sub, mul, div, "div입니다.")
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)


dfs(1, nums[0], add, sub, mul, div)
print(maxV)
print(minV)
