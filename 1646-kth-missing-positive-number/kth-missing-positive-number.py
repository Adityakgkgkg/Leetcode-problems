class Solution(object):
    def findKthPositive(self, arr, k):
        n = len(arr)
        for i in range(n):
            if arr[i] > (i + k):
                return i + k
        return n + k
        