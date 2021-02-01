def solution(d, budget):
    d.sort()
    result = 0
    while sum(d) > budget:
        d.pop()
    return len(d)
