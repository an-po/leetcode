class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        Z = ['' for i in range(min(len(s),numRows))]
        i = 0
        di = 1
        for ch in s:
            Z[i] += ch
            if i == 0: di = 1
            if i == numRows-1: di = -1
            i += di
        R = ''.join(Z)
        return R