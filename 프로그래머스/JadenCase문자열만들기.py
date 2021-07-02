def solution(s):
    answer = ''
    new_s = s.split(' ')
    for i in range(len(new_s)):
        answer += new_s[i][:1].upper() + new_s[i][1:].lower() + ' '

    answer = answer[:-1]
    return answer
