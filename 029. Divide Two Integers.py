class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            neg = True
        else:
            neg = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            tmp = divisor
            res = 1
            while tmp <= dividend:
                tmp = tmp << 1
                res = res << 1
            tmp = tmp >> 1
            res = res >> 1
            result += res
            dividend = dividend - tmp
        if neg:
            result = -result
        return result

s = Solution()
print(s.divide(-2147483648, -1))