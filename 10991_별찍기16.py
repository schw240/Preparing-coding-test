N = int(input())
b,c = N,N
for i in range(N):
    print("{0}{1}{2}".format(" "*(b-1-i), "*", " *"*i))
    