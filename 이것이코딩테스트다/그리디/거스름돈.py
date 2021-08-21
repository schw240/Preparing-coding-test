n = 1260
cnt = 0

coins = [500, 100, 50, 10]

for coin in coins:
    cnt += n // coin  # 몫 더해주기
    n = n % coin  # n 나눠주기


print(cnt)
