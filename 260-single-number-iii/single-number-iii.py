class Solution(object):
    def singleNumber(self, arr):
        n= len(arr)
        x = 0
        for i in range(n):
            x ^= arr[i]
        x = x & (-x)
        a = 0
        b =0
        for i in range(n):
            if arr[i] & x ==x:
                a ^= arr[i]
            else:
                b ^=arr[i]
        return [a,b]
        