n = int(input())

factorial = [1 for _ in range(n+1)]

for i in range(1, n+1):
    factorial[i] = i*factorial[i-1]


result = 0
check = 1
while check:
    if factorial[n] % 10 == 0:
        factorial[n] //= 10
        result += 1
    else:
        check = 0


print(result)
