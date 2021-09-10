class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        r = 0
        i = 0
        while (s != '' and s[0] == ' '):
            s = s[1:]
        if (s != '' and s[0] == '-'):
            sign = -1
            s = s[1:]
        elif (s != '' and s[0] == '+'):
            sign = 1
            s = s[1:]
        while (s != '' and s[0] in '0123456789'):
            r = r * 10 + int(s[0])
            s = s[1:]
        r = r * sign
        if r < -2147483648:
            r = -2147483648
        if r > 2147483647:
            r = 2147483647
        return r