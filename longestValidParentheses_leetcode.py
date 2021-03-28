class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        # l 괄호가 유효한 시퀀스를 형성하는 문자열의 위치를 보유
        # 0 유효하지 않음을 의미하고 1은 유효한 시퀀스를 의미
        l = ['0'] * len(s)
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                # 스택에 "("의 인덱스 추가
                stack.append(i)
            else:
                # 최신 스택 요소가 양수이면 "("괄호)
                # 그것을 팝하고 ㅣ의 값을 유효한 값 1으로 대체
                if stack and stack[-1] >= 0:
                    l[stack.pop()] = '1'
                    l[i] = '1'
                else:
                    # 그렇지 않으면 ")" 괄호를 의미하는 음수 값을 추가
                    stack.append(-1)

        return len(max(''.join(l).split('0')))
