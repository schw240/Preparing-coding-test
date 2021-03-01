class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAXNUM = 2**31-1
        MINNUM = -2**31

        if dividend == 0:
            return 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        divisor2 = divisor
        result = 0
        term = 1
        # print("1", dividend, divisor, divisor2, result)
        while True:
            if dividend < divisor2:
                break
            dividend -= divisor2
            result += term

            divisor2 += divisor2
            term += term
        # print("2", dividend, divisor, divisor2, result)
        result += self.divide(dividend, divisor)

        if sign*result > MAXNUM:
            return MAXNUM
        elif sign*result < MINNUM:
            return MINNUM
        else:
            return sign*result
