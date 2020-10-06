N = int(input())
j = N-1
for i in range(1,N):
    print("{0}{1}{2}".format("*"*i, " "*((2*j)), "*"*i))
    j -= 1
print("*"*(2*N))
j = N - 1
for i in range(1, N):
    print("{0}{1}{2}".format("*"*j, " "*(2*(i)), "*"*j))
    j -= 1