N = int(input())
# 도로의 길이
lengths = (list(map(int, input().split(' '))))
# 주유소의 리터당 가격
oil_prices = (list(map(int, input().split(' '))))

# 첫번째 도로에서는 두번째 도로까지 갈만큼의 양을 넣어야함
min_price = oil_prices[0]
total = 0

for i in range(N-1):
    if oil_prices[i] >= min_price:
        total += min_price * lengths[i]
    else:
        min_price = oil_prices[i]
        total += min_price * lengths[i]
print(total)
