from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def get_list(n):
            if n == 0:
                return list([])
            lsts = list()
            for item in m[n]:
                i_lsts = get_list(item[0])
                for i_lst in i_lsts:
                    i_lst.extend(item[1])
                lsts.extend(i_lsts)
            return lsts

        nums = sorted(candidates)
        m = dict()
        for i in range(1, target + 1):
            m[i] = list()
        for x in nums:
            m[x].append((0, x))
            for i in range(x + 1, target + 1):
                if len(m[i - x]) != 0:
                    m[i].append((i - x, x))
        return get_list(target)


s = Solution()
candidates = [2, 3, 5]
target = 18
print(s.combinationSum(candidates, target))
