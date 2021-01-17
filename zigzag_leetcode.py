class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        lines = ['' for i in range(numRows)]

        if numRows == 1:
            return s
        else:
            for i in range(len(s)):
                modnum = numRows-1
                if i%(modnum*2) < modnum:
                    lines[i%modnum] += s[i]
                else:
                    lines[modnum-i%modnum] +=s[i]
            result = ''
            for i in range(len(lines)):
                result += lines[i]
            return result
print(Solution().convert("PAYPALISHIRING", 3))