import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        min_heap = []
        
        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        
        return [num for freq, num in min_heap]
        