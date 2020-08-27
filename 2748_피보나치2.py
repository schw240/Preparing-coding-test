# recursive call
def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)

# 동적계획법 사용

def fibo_dp(num):
    memo = [0 for index in range(num + 1)]
    memo[0] = 0
    memo[1] = 1

    for i in range(2, num+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[num]

# 백준 2748 피보나치 2
num = int(input())

memo = [0 for index in range(num + 1)]
memo[0], memo[1] = 0, 1

for i in range(2, num+1):
    memo[i] = memo[i-1] + memo[i-2]
 
print(memo[num])