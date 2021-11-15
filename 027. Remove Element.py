class Solution:
    def removeElement(self, nums, val):
        i = -1
        j = len(nums) - 1
        while i < j:
            i += 1
            if nums[i] == val:
                while (j > i) and (nums[j] == val):
                    j -= 1
                if j > i:
                    nums[i] = nums[j]
                else:
                    return i
                j -= 1
        return i + 1

s = Solution()
nums = [0]
val = 0
print(s.removeElement(nums, val))
print(nums)