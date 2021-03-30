# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현
# aabbaccc 면 2a2ba3c 이런식 숫자가 앞으로 한개인 경우는 숫자 생략
# 숫자를 늘려가며 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution함수 작성
# 자르고 남은 문자열은 그냥 맨뒤에 붙여주기
def solution(s):
    answer = []
    res = ""

    if len(s) == 1:
        return 1

    # 절반 이상은 넘지 않을것이므로 num개씩 자르기
    for num in range(1, len(s)//2+1):
        tmp = s[:num]  # 맨 처음 비교군
        cnt = 1  # 개수 비교
        # num개씩 비교
        for i in range(num, len(s), num):
            if s[i:i+num] == tmp:  # 다음 자른값과 같으면
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""  # 1개면 그냥 안붙임
                res += str(cnt) + tmp
                tmp = s[i:i+num]  # tmp 갱신
                cnt = 1
        print(tmp, "추가전 tmp")

        res += str(cnt) + tmp
        answer.append(len(tmp))
        tmp = ""
        # 중간에 num이 바뀌는거같은데... 뭐가 문제일까..

    return min(answer)


print(solution("aabbaccc"))
