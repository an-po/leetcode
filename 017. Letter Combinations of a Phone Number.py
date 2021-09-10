class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        dig = dict()
        dig['2'] = ['a', 'b', 'c']
        dig['3'] = ['d', 'e', 'f']
        dig['4'] = ['g', 'h', 'i']
        dig['5'] = ['j', 'k', 'l']
        dig['6'] = ['m', 'n', 'o']
        dig['7'] = ['p', 'q', 'r', 's']
        dig['8'] = ['t', 'u', 'v']
        dig['9'] = ['w', 'x', 'y', 'z']
        if len(digits) == 1:
            return dig[digits]
        ch = digits[0]
        l = self.letterCombinations(digits[1:])
        ll = list()
        for item in l:
            for i in range(len(dig[ch])):
              ll.append(dig[ch][i] + item)
        return ll