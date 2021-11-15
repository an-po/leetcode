class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            av = (left + right) // 2
            if nums[av] > nums[right]:
                left = av
            else:
                right = av
        k = left

        if (target >= nums[0]) and (target <= nums[k]):
            left = 0
            right = k
            while left < right:
                av = (left + right) // 2
                if target > nums[left]:
                    left = av + 1
                else:
                    right = av
            if nums[left] == target:
                return left
            else:
                return - 1

        if (k < len(nums) - 1) and (target >= nums[k + 1]) and (target <= nums[-1]):
            left = k + 1
            right = len(nums) - 1
            while left < right:
                av = (left + right) // 2
                if target > nums[av]:
                    left = av + 1
                else:
                    right = av
            if nums[left] == target:
                return left
            else:
                return - 1

        return -1



s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
print(s.search(nums, target))