def solution(s):
    answer = True

    stack = []

    for ch in s:
        if ch == '(':
            stack.append('(')
        else:
            try:
                stack.pop()
            except:
                return False

    if len(stack) == 0:
        return True
    else:
        return False
