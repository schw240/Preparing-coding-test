# 문자열 S(0과 1로만 이루어진)에 있는 모든 숫자를 전부 같게 만들려고 함
# S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는것(0을 1로 1을 0으로)

S = input()

zero_cnt = 0
one_cnt = 0
compare = S[0]
# 맨 처음 경우 더해주기
if compare == '1':
    one_cnt += 1
else:
    zero_cnt += 1

for i in range(1, len(S)):
    if compare != S[i] and S[i] == '0':
        # compare 1이란 뜻
        # 0 증가 후 compare 바꿔주기
        zero_cnt += 1
        compare = '0'
    elif compare != S[i] and S[i] == '1':
        # compare이 0이란 뜻
        one_cnt += 1
        compare = '1'

print(min(zero_cnt, one_cnt))
