class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mul(num, dgt):
            mem = 0
            result = ''
            for ch in num[::-1]:
                m = int(ch) * int(dgt) + mem
                if (m != 0) or (mem != 0):
                    result = str(m % 10) + result
                    mem = m // 10
            if mem > 0:
                result = str(mem) + result
            return result

        def add(num1, num2):
            i = 1
            mem = 0
            result = ''
            if len(num1) > len(num2):
                num2 = '0' * (len(num1) - len(num2)) + num2
            else:
                num1 = '0' * (len(num2) - len(num1)) + num1
            while (i <= len(num1)):
                s = int(num1[-i]) + int(num2[-i]) + mem
                result = str(s % 10) + result
                mem = s // 10
                i += 1
            if mem > 0:
                result = str(mem) + result
            return result

        result = '0'
        dec = ''
        for ch in num1[::-1]:
            m = mul(num2, ch)
            if m != '0':
                m = m + dec
            result = add(result, m)
            dec = dec + '0'
        while len(result) > 1 and result[0] == '0':
            result = result[1:]

        return result



s = Solution()
num1 = "9133"
num2 = "0"
print(s.multiply(num2, num1))