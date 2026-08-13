class Solution(object):
    def binaryGap(self, n):
        prev = -1
        pos = 0
        ans = 0

        while n:
            if n & 1:
                if prev != -1:
                    ans = max(ans,pos - prev)
                prev = pos
            n >>=1
            pos +=1
        return ans
            
        