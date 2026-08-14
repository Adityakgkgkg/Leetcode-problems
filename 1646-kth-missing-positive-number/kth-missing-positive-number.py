class Solution(object):
    def findKthPositive(self, arr, k):
        n = len(arr)
        low = 0
        high = n - 1
        res = n + k
        while low <=high:
            mid = (low + high) // 2
            if arr[mid] > mid + k:
                res = mid + k
                high = mid -1
            else:
                low = mid + 1
        return res
        