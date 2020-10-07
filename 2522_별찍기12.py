N = int(input())
j = N
for i in range(1, N+1):
    print("{0}{1}".format(" "*(N-1), "*"*i))
    N -= 1
for i in range(1, j):
    print("{0}{1}".format(" "*i, "*"*(j-1)))
    j -= 1