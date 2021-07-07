def gcd(A, B):
    while B:
        A, B = B, A % B
    return A


def lcm(A, B):
    return A * B // gcd(A, B)


for i in range(int(input())):
    A, B = map(int, input().split(' '))
    print(lcm(A, B))
