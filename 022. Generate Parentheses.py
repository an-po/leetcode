class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['()']
        else:
            s = list()
            subs = self.generateParenthesis(n - 1)
            for item in subs:
                s.append('(' + item + ')')
            for i in range(1, n):
                subs1 = self.generateParenthesis(i)
                subs2 = self.generateParenthesis(n-i)
                for item1 in subs1:
                    for item2 in subs2:
                        s.append(item1 + item2)
            s = set(s)
            s = list(s)
            return s