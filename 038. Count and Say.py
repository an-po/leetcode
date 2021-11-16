class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for k in range(2, n + 1):
            next_s = ''
            last_ch = ''
            count = 0
            for ch in s:
                if ch == last_ch:
                    count += 1
                else:
                    if last_ch != '':
                        next_s = next_s + str(count) + last_ch
                    last_ch = ch
                    count = 1
            s = next_s + str(count) + last_ch
        return s


s = Solution()
print(s.countAndSay(30))