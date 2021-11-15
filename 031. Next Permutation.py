class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while (i > 0) and (nums[i - 1] >= nums[i]):
            i -= 1
        if i == 0:
            nums.sort()
        else:
            j = len(nums) - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
            for x in range(len(nums) - 1, i, -1):
                for y in range(i + 1, x + 1):
                    if nums[y - 1] > nums[y]:
                        nums[y - 1], nums[y] = nums[y], nums[y - 1]


s = Solution()
nums = [5, 4, 7, 5, 3, 2]
s.nextPermutation(nums)
print(nums)