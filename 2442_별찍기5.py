N = int(input())
i = 1
while N > 0:
    print("{0}{1}{2}".format(" "*(N/2), "*"*(2*i - 1), " "*(N/2)))
    N -= 1
    i += 1