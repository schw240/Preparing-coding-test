def solution(n):
    answer = 0
    res = ''
    while n >= 1:
        rest = n % 3
        n //= 3
        res += str(rest)
    answer = int(res, 3)
    return answer
