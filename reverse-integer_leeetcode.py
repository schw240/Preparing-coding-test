class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        if x > 0:
            ans = int(str(x)[::-1])
        if x < 0:
            ans = ((-1) * (int(str(x*(-1))[::-1])))
        #변한 값이 범위를 벗어나면
        if ans not in range(-2**31, 2**31):
            ans = 0
        return ans
print(Solution().reverse(1534236469))