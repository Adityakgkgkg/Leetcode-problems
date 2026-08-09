class Solution(object):
    def maxDistance(self, arr, m):
        arr.sort()
        low = 1
        high = arr[-1] - arr[0]
        
        def canplace(distance):
            count = 1
            last = arr[0]
            
            for i in range(1,len(arr)):
                if arr[i] - last >= distance:
                    count +=1 
                    last = arr[i] 
                    
                    if count == m:
                        return True
            return False
        
        while low <= high:
            mid = (low + high) // 2
            
            if canplace(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high        
        