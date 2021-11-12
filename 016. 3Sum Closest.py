class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums = sorted(nums)
        closest = sum(nums[:3])
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if abs(target - tmp) < abs(target - closest):
                    closest = tmp
                if tmp > target:
                    k -= 1
                else:
                    j += 1
        return closest




s = Solution()
nums = [-1, 2, 1, -4]
nums = [1, 2, 5, 10, 11]
target = 12
print(s.threeSumClosest(nums, target))