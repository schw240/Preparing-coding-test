N = int(input())
space = " "
for i in range(1,N+1):
    print("{0}{1}".format(space*(N-i),'*'*i))