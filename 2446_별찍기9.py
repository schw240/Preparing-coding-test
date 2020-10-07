N = int(input())
j = N
for i in range(0, N):
    print("{0}{1}".format(" "*i, "*"*(2*N - 1)))
    N -= 1
for i in range(2,j+1):
    print("{0}{1}".format(" "*(j-2), "*"*(2*i - 1)))
    j -= 1