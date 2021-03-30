# 현재 캐릭터의 점수를 N
# 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자리수의 합과 오른쪽 부분의 각 자리수의 합을 더한 값이
# 동일할때

N = int(input())
str_N = str(N)
left = str_N[:len(str_N)//2]
right = str_N[len(str_N)//2:]

left_sum, right_sum = 0, 0
for i in range(len(left)):
    left_sum += int(left[i])
    right_sum += int(right[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
