def solution(n):
    answer = []
    new_n = str(n)[::-1]
    for i in range(len(new_n)):
        answer.append(int(new_n[i]))
    return answer
