N = int(input())
i = 0
while N > 0:
    print("{0}{1}".format(" "*i,"*"*N))
    N -= 1
    i += 1