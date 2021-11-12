class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        k = 0
        while i < len(nums):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
            i += 1
        return k + 1

nums = list((1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 7, 7))
s = Solution()
print(s.removeDuplicates(nums))
print(nums)
