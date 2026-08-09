class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        def canFinish(k):
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            return hours <= h

        while low <= high:

            mid = (low + high) // 2

            if canFinish(mid):
                high = mid - 1   
            else:
                low = mid + 1       

        return low
        