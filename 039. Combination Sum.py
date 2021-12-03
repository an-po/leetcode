from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()
        def RS(cur, total, i):
            nonlocal ans
            if i >= len(candidates) or total > target:
                return []
            if total == target:
                ans.append(cur.copy())
                return
            for j in range(i, len(candidates)):
                cur.append(candidates[j])
                RS(cur, total + candidates[j], j)
                cur.pop()

        RS([], 0, 0)
        return ans


class Solution2:
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
candidates = [2, 3, 6, 7]
target = 7

print(s.combinationSum(candidates, target))
