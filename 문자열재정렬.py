# 문자열 입력
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에 모든 숫자를 더한값을 이어서 출력

S = input()
alpha = []
number = 0

for i in range(len(S)):
    if S[i].isalpha():
        alpha.append(S[i])
    else:
        number += int(S[i])


alpha.sort()

#print(alpha, number)
print(''.join(alpha) + str(number))
