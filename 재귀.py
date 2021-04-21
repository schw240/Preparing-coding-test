def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num-1)

# 숫자가 들어있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요


def sum_list(data):
    if len(data) == 1:
        return data[0]
    return data[-1] + sum_list(data[:-1])


def palindrome(str):
    if len(str) <= 1:
        return True

    if str[0] == str[-1]:
        return palindrome(str[1:-1])
    else:
        return False


# print(palindrome("MOMOM"))

# 홀수이면 3 * n + 1 짝수이면 n // 2
def solution(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 1:
        return solution(n * 3 + 1)
    elif n % 2 == 0:
        return solution(n // 2)


# print(solution(3))

# 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수
# f(n)은 f(n-1) + f(n-2) + f(n-3) 과 동일하다는 패턴 찾기

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return f(n-1) + f(n-2) + f(n-3)


print(f(5))
