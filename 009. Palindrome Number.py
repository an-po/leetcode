class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xx = x
        x_invert = 0
        while xx != 0:
            x_invert = x_invert * 10 + xx % 10
            xx = xx // 10
        return x == x_invert
