class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_d = dict()
        start_i = 0
        for i in range(len(s)):
            if char_d.get(s[i]) is not None:
                max_length = max(max_length, i - start_i)
                start_i = max(char_d[s[i]] + 1, start_i)
            char_d[s[i]] = i
        max_length = max(max_length, len(s) - start_i)
        return max_length

s = Solution()
print(s.lengthOfLongestSubstring('abba'))



