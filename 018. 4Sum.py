class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    tmp = nums[i] + nums[j] + nums[k] + nums[l]
                    if tmp > target:
                        l -= 1
                    elif tmp < target:
                        k += 1
                    else:
                        ans.add((nums[i], nums[j], nums[k], nums[l]))
                        l -= 1
                        k += 1
        return list(ans)




s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
#nums = [2, 2, 2, 2, 2]
#target = 8
nums = [-3,-2,-1,0,0,1,2,3]
target = 0
print(s.fourSum(nums, target))

