# (n)  ==> nCk = n! / ((n-k)! * k!) 이항계수와 조합이 같은개념 같다
# (k)

n, k = map(int, input().split())


def fac(a):  # k가 입력값으로 0이 들어올 수 있으므로 0에대한 처리도 해줘야한다.
    if a == 0:
        return 1
    if a == 1:
        return 1
    else:
        return a * fac(a-1)


print(fac(n) // (fac(n-k) * fac(k)))
