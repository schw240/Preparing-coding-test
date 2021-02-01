import math


def solution(n):
    answer = 0
    print(int(math.sqrt(n)))
    if math.sqrt(n) == int(math.sqrt(n)):
        return (int(math.sqrt(n)) + 1) ** 2
    else:
        return -1
