from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        m = dict()
        for x in nums:
            for i in range(1, target // x + 1):
                m[i * x].append()

s = Solution()
candidates = [2, 3, 5]
target = 8
s.combinationSum(candidates, target)
