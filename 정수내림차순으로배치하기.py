def solution(n):
    n = str(n)
    tmp = []
    for i in range(len(n)):
        tmp.append(n[i])
    tmp.sort(reverse=True)
    return int("".join(tmp))
