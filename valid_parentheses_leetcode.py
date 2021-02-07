class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'}': '{', ')': '(', ']': '['}

        for bracket in s:
            # 여는 괄호인경우
            if bracket in brackets.values():
                stack.append(bracket)
            # 닫는 괄호인 경우
            else:
                if stack and brackets[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True
