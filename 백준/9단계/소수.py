M = int(input())
N = int(input())

# M 이상 N 이하의 자연수 중 소수인 것을 모두 골라 이들의 합, 최소값 반환


def isPrimeNum(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


primes = []
for i in range(M, N+1):
    if isPrimeNum(i) == True:
        primes.append(i)

if primes:
    print(sum(primes), min(primes))
else:
    print(-1)
