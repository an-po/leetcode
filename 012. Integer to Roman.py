class Solution(object):
    def intToRoman(self, num):
        ara = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        rom = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        roman = ''
        for i in range(len(ara)):
            while num >= ara[i]:
                roman = roman + rom[i]
                num = num - ara[i]
        return roman
