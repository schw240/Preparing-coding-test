N = int(input())
b = N
for i in range(1,N+1):
    if i == 1:
        print(" "*(b-i)+"*")
    elif i == N:
        print("*"*(2*N - 1))
    else:
        print("{0}{1}{2}{3}".format(" "*(b-i), "*"," "*(2*i-3), "*"))
