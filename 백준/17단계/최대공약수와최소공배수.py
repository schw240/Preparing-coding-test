A, B = map(int, input().split(' '))


def gcd(A, B):
    while B:
        A, B = B, A % B
    return A


def lcm(A, B):
    return A * B // gcd(A, B)


print(gcd(A, B))
print(lcm(A, B))
