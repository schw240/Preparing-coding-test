class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
            # ans holds the places in the string where parenthesis form a valid sequence.
        # 0 means invalid and 1 means valid sequence.
        ans = ['0'] * len(s)
        stack = []
        for i, v in enumerate(s):
            if v == '(':
                # append index of "(" into the stack
                stack.append(i)
            else:
                # if latest stack element is positive, it means it was a "(" parenthesis
                # pop it and substitute values in "l" for the given indexes to valid values ("1")
                if stack and stack[-1] >= 0:
                    ans[stack.pop()] = '1'
                    ans[i] = '1'
                else:
                    # otherwise, append a negative value, meaning it's a ")" closing parenthesis.
                    stack.append(-1)
        # compute the longes sequence of "1" in l.
            print(stack)
        return len(max(''.join(ans).split('0')))
