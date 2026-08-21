class Solution(object):
    def intersect(self, nums1, nums2):
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num,0) + 1
        res = []
        for num in nums2:
            if freq.get(num,0) > 0:
                res.append(num)
                freq[num] -= 1
        return res


        