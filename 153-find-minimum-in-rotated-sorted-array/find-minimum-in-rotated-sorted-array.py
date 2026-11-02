class Solution(object):
    def findMin(self, nums):
        min = float('inf')
        for num in nums:
            if num <= min:
                min = num
        return min       