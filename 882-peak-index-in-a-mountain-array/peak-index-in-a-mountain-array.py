class Solution(object):
    def peakIndexInMountainArray(self, arr):
        n = len(arr)
        left = 0
        right = n-1
        while left < right :
            mid =(left + right) // 2
            if arr[mid] > arr[mid+1]:
                right = mid
            else:
                left = mid+1
        return left


        