class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        counts = dict()
        ans = list()
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if (i == 0) or (nums[i] != nums[i - 1]):
                counts[nums[i]] -= 1
                for j in range(i + 1, len(nums)):
                    if (j == i + 1) or (nums[j] != nums[j - 1]):
                        x = 0 - nums[i] - nums[j]
                        if (x < 0) or (x < nums[j]):
                            break
                        counts[nums[j]] -= 1
                        if counts.get(x, 0) > 0:
                            ans.append((nums[i], nums[j], x))
                        counts[nums[j]] += 1
        return ans



s = Solution()
nums = [-1, 0, 0, 1, 2, 1, -1, -4]
print(s.threeSum(nums))