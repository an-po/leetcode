class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        allans = list()
        ans = {}
        item = list()
        for i in range(len(nums)):
            ans[nums[i]] = ans.get(nums[i], 0) + 1
        for i in range(len(nums)):
            if (i == 0) or (nums[i] != nums[i-1]):
                a = nums[i]
                if (a > 0): break;
                ans[a] -= 1
                j = i + 1
                while (j < len(nums)):
                    if (nums[j] != nums[j-1] or j - i == 1):
                        b = nums[j]
                        c =  0 - a - b
                        if ((c < 0) or (c < b)): break
                        ans[b] -= 1
                        if ans.get(c, 0) > 0:
                            #if ([a, b, c] not in allans):
                            allans.append([a, b, c])
                        ans[b] += 1
                    j += 1
                ans[a] += 1
        return allans