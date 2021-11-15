class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            av = (left + right) // 2
            if target > nums[av]:
                left = av + 1
            else:
                right = av
        first = left
        if nums and nums[first] == target:
            left = first
            right = len(nums) - 1
            while left < right:
                av = (left + right) // 2 + 1
                if nums[av] > target:
                    right = av - 1
                else:
                    left = av
            last = left
            return (first, last)
        else:
            return (-1, -1)

s = Solution()
nums = [1]
target = 1
print(s.searchRange(nums, target))