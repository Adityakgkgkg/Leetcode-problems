
def merge(intervals):
        #intervals.sort(key=lambda x: x[0])
    intervals.sort()
    res = []
    res.append(intervals[0])
    for i in range(1,len(intervals)):
        last = res[-1]
        curr = intervals[i]
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    return res
class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        return merge(intervals)
        