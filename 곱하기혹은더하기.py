# 왼쪽부터 오른쪽으로 숫자를 확인하며 X 혹은 + 연산자를 넣어 만들 수 있는 가장 큰 수 구하는 프로그램
# 만약 0이 있다면 더하고 나머지는 곱하기?

S = input("숫자를 문자로 입력:")

i = 1
res = int(S[0])

while i < len(S):
    # 맨 앞 숫자가 0이나 1이라면 + 아니면 *(res)
    # S[i]에서도 1이나 0이 들어올때
    if res <= 1 or int(S[i]) <= 1:
        res += int(S[i])
        i += 1
    else:
        res *= int(S[i])
        i += 1
print(res)
