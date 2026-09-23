class Solution(object):
    def missingNumber(self, arr):
        n = len(arr)
        x = 0
        for num in range(1,n+1):
            x ^= num
        for num in arr:
            x ^= num
        return x
        