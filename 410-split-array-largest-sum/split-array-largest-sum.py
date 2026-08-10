class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)

        def canSplit(limit):
            count = 1
            current = 0

            for num in nums:
                if current + num <= limit:
                    current += num
                else:
                    count += 1
                    current = num

            return count <= k

        while low <= high:

            mid = (low + high) // 2

            if canSplit(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
        