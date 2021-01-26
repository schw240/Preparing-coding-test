def solution(n):
    answer = ''
    s1 = "수"
    s2 = "박"
    for i in range(n):
        if i % 2 == 0:
            answer += s1
        else:
            answer += s2
    return answer
