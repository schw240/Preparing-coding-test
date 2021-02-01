def solution(s, n):
    answer = ''

    for i in range(len(s)):
        tmp = 0
        if s[i].isupper():
            tmp = ((ord(s[i]) - ord('A') + n) % 26) + ord('A')
            answer += chr(tmp)
        elif s[i] == " ":
            answer += " "
        elif s[i].islower():
            tmp = ((ord(s[i]) - ord('a') + n) % 26) + ord('a')
            answer += chr(tmp)

    return answer
