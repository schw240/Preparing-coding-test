M, N = map(int, input().split(' '))


def isPrime(num):
    if num < 2:
        return False
    # 제곱근까지만 검사했을때 걸리면 소수 아님
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


for i in range(M, N+1):
    if isPrime(i) == True:
        print(i)
