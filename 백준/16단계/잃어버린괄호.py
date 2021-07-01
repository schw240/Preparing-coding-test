S = input().split('-')
# 최소값을 구하기
# -를 만나기 전까지 모든 값을 더해줌

res = 0

# S[0]안에 있는 값은 - 만나기 전 숫자들 다 더해주기
for num in S[0].split('+'):
    res += int(num)

# S[1]부터 다시 계산하기
for num in S[1:]:
    for num2 in num.split('+'):
        res -= int(num2)

print(res)
