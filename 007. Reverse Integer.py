class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        s = 1 if x > 0 else -1
        x = abs(x)
        while x != 0:
            r = r * 10 + x % 10
            x = x // 10
        r = r * s
        if (r < - 2 ** 31) or (r > 2 ** 31 - 1):
            r = 0
        return r