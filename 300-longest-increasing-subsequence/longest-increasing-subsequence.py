class Solution(object):
    def lengthOfLIS(self, nums):
        arr = []
        for num in nums:
            left = 0
            right = len(arr)

            while left < right:
                mid = (left + right) // 2

                if arr[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(arr):
                arr.append(num)
            else:
                arr[left] = num
        return len(arr)

        