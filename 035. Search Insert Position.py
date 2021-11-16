from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target):
        if nums[0] > target:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            av = (left + right) // 2 + 1
            if nums[av] > target:
                right = av - 1
            else:
                left = av
        if nums[left] == target:
            return left
        else:
            return left + 1


s = Solution()
nums = [1, 3, 5, 6]
target = 0
print(s.searchInsert(nums, target))

