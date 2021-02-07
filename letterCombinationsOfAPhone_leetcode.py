class Solution:
    # 숫자별 알파벳 받아와 조합 만들어주기
    def twoCombinations(self, chlist1, chlist2):
        output = []
        for i in range(len(chlist1)):
            ch1 = chlist1[i]
            for k in range(len(chlist2)):
                ch2 = chlist2[k]
                output.append(ch1+ch2)

        return output

    def letterCombinations(self, digits: str) -> List[str]:
        output = []

        if len(digits) == 0:
            return []

        digitchr = {}
        chrlist = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # 딕셔너리로 만들기
        for i, ch in enumerate(chrlist):
            digitchr[i+2] = ch

        numlist = []
        # 알파벳만 빼오기
        for m in range(len(digits)):
            numlist.append(digitchr[int(digits[m])])

        previouslist = numlist[0]
        ans = []

        if len(digits) == 1:
            for i in range(len(previouslist)):
                ans.append(previouslist[i])
            return ans

        for m in range(1, len(numlist)):
            previouslist = self.twoCombinations(previouslist, numlist[m])

        return previouslist
