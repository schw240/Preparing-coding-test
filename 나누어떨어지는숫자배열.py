def solution(arr, divisor):
    answer = []
    for e in arr:
        if(e % divisor == 0):
            answer.append(e)
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        answer.sort()
        return answer


def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]
