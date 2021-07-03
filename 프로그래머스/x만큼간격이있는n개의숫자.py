def solution(x, n):
    answer = []

    num = 0
    for i in range(n):
        num = num + x
        answer.append(num)
    return answer
