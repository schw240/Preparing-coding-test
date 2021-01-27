class Solution:
    def romanToInt(self, s: str) -> int:
        # 큰수 왼쪽부터 작은수 순
        dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        answer = 0
        for i in range(len(s)-1):
            # 4는 5에서 1뺀것, 9는 10에서 1뺀것 (1 I)
            # 40은 50에서 10뺀것, 90은 100에서 10뺀것 (10 X)
            # 400은 500에서 100뺀것 900은 1000에서 100뺀것 (100 C)
            # 문자 2개 비교
            cur_num = dic[s[i]]
            next_num = dic[s[i+1]]
            if cur_num >= next_num:
                answer += cur_num
            else:
                answer -= cur_num
        answer += dic[s[len(s)-1]]

        return answer
