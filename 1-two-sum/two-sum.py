class Solution(object):
    def twoSum(self, nums, target):
        s = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in s:
                return [s[complement], i]
            s[nums[i]] = i
        return []
        