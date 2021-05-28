N = int(input())
nums = list(map(int, input().split(' ')))

cnt = 0
for num in nums:
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
        if error == 0:
            cnt += 1


# 소수는 1과 자기 자신으로 나눌때만 나누어 떨어지는 자연수

print(cnt)
