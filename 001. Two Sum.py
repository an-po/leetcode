class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_d = dict()
        for i in range(len(nums)):
            if nums_d.get(target - nums[i]) is not None:
                return nums_d[target - nums[i]], i
            else:
                nums_d[nums[i]] = i
