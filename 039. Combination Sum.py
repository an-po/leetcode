from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()

        def RS(cur, total, i):
            if total > target or i >= len(candidates):
                return
            if total == target:
                ans.append(cur.copy())
                return
            RS(cur, total, i + 1)
            cur.append(candidates[i])
            RS(cur, total + candidates[i], i)
            cur.pop()
        candidates.sort()
        RS([], 0, 0)
        return ans


s = Solution()
candidates = [2, 3, 5]
target = 18
print(s.combinationSum(candidates, target))
