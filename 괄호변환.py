def split(p):
    # open과 close의 갯수가 맞으면 반환
    openBracket = 0
    closeBracket = 0
    u = ""
    for i in range(len(p)):
        item = p[i]
        if item == "(":
            openBracket += 1
        else:
            closeBracket += 1
        u += p[i]
        # 둘의 갯수가 같아지면 종료
        if openBracket == closeBracket:
            return u, p[i+1:]  # p는 u가 아닌부분
    # 반복문을 돌아도 안걸렸다면 empty
    return p, ""


p = "asd"
# 스택에 넣어서 짝이 맞는지 확인


def right(p):
    stack = []
    for bracket in p:
        if bracket == "(":
            stack.append(bracket)
        else:  # 닫힌괄호
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    return False


def reverse(p):
    res = ""
    for item in p:
        if item == "(":
            res += ")"
        else:
            res += "("
    return res


def solve(p):
    # 1. 빈문자열 반환
    if p == "":
        return ""

    # 2. w를 균형잡힌 괄호 문자열로 분리
    u, v = split(p)

    # 3. 문자열 u가 올바른 괄호 문자열인 경우
    if right(u):
        # 3. 문자열 v를 1단계부터 수행
        # 수행한 결과를 u에 이어붙여 반환
        return u + solve(v)
    # 4. 올바른 괄호 문자열이 아닌경우
    else:
        # 4-1 빈 문자열에 첫 번째 문자로 (를 붙임
        empty = "("
        # 4-2 v를 재귀적으로 수행한 결과를 이어붙인다
        empty += solve(v)
        # 4-3 )를 다시 붙인다.
        empty += ")"
        # 4-4 u의 맨 앞과 뒷문자 제거하고
        u = u[1:-1]
        # 나머지 문자열의 괄호 방향을 뒤집는다
        u = reverse(u)
        return empty + u


def solution(p):
    # 균형잡힌 괄호 문자열이면 -> # 올바른 괄호 문자열로 변환 가능
    # 균형잡힌 괄호 문자열은 갯수만 맞는경우
    # 올바른 괄호 문자열은 갯수와 괄호의 짝도 모두 맞는 경우
    '''
    1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u     는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈    문자열이 될 수 있습니다. 
    3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
      3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
    4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
      4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
      4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
      4-3. ')'를 다시 붙입니다. 
      4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
      4-5. 생성된 문자열을 반환합니다.'''
    return solve(p)


print(solution("(()())()"))
