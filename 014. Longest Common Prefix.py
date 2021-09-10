class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        minlen = len(strs[0])
        for str in strs:
            if len(str) < minlen:
                minlen = len(str)

        maxpref = ''
        for i in range(minlen):
            pref = strs[0][:i+1]
            for str in strs:
                if not str.startswith(pref):
                    break
            if str.startswith(pref):
                maxpref = pref

        return maxpref