# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액중 최소값

N = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1  # 금액 1로 처음에 만들수 있는지 확인하기 위해 1로 설정

for i in range(len(coins)):
    # 계속 더해가면서 만들수있는지?
    #
    if target < coins[i]:  # 맨처음 1인지?랑 그 뒤부터 더하면서 만들 수 있는지 확인
        break
    target += coins[i]

print(target)
