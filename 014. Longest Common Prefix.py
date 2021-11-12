class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        max_pref = strs[0]
        for str in strs[1:]:
            i = 0
            min_len = min(len(str), len(max_pref))
            while (i < min_len) and (str[i] == max_pref[i]):
                i += 1
            if i == 0:
                return ''
            max_pref = max_pref[:i]
        return max_pref

s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight", ""]))