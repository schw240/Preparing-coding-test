def solution(n):
    answer = 0
    new_n = str(n)
    for i in range(len(new_n)):
        answer += int(new_n[i])
    return answer
