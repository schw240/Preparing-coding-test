"""
GCD(Greatest Common Divider)
LCM(Least Common Multiple)
이 2가지는 가장 많이 나오는 유형
최대 공약수 / 최소 공배수문제는 이 알고리즘 활용

LCM(a, b) = a * b / GCD(a, b)
GCD(a, b) = GCD(b, a % b)
"""

# 방법 1 : 단순 반복문 사용해 GCD 구현
import math


def gcd_native(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# 방법 2-1: 유클리드호제법 이용


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

# 방법 2-2: 반복문으로 변경


def gcd2(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


# 방법 3: math의 gcd 사용하기
math.gcd(1, 2)
