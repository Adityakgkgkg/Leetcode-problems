class Solution(object):
    def subarraySum(self, nums, k):
        prefixsum = {}
        res = 0
        currsum = 0

        for val in nums:
            currsum += val

            if currsum == k:
                res += 1
            if currsum - k in prefixsum:
                res += prefixsum[currsum - k]
            
            prefixsum[currsum] = prefixsum.get(currsum , 0) + 1
        return res
        