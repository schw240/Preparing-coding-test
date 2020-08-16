def solution(N, number):
    S = [{N}]
    #print(S)
    for i in range(2, 9):
        lst = [int(str(N)*i)]
        for j in range(int(i / 2)):
            for x in S[j]:
                for y in S[i - j - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1
