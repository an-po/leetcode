class Solution(object):
    def isMatch(self, s, p):
        if (p == ''):
            return s == ''
        ch_match = (len(s) > 0) and (s[0] == p[0] or p[0] == '.')
        if (len(p) >= 2 and (p[1] == '*')):
            if len(s) > 0:
                if ch_match:
                    return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                else:
                    return self.isMatch(s, p[2:])
            else:
                return self.isMatch('', p[2:])
        else:
            return ch_match and self.isMatch(s[1:], p[1:])