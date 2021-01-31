class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
               50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        answer = ""

        while num != 0:
            for d in dic:
                if num - d >= 0:
                    answer += dic[d]
                    num -= d
                    break

        return answer
