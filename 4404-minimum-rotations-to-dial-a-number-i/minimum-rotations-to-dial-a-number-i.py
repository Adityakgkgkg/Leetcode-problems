class Solution(object):
    def minRotations(self, s):
        n = len(s)
        current = 0
        ans = 0
        for i in range(n):
            digit = int(s[i])
            diff = abs(current -  digit)
            rotation = min(diff, 10 - diff)
            ans +=rotation
            current = digit
        return ans
        