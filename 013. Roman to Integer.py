class Solution(object):
    def romanToInt(self, s):
        ara = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        rom = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        num = 0
        for i in range(len(ara)):
            while s.startswith(rom[i]):
                num = num + ara[i]
                s = s[len(rom[i]):]
        return num