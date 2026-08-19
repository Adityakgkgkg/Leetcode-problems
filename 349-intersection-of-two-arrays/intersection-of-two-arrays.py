class Solution(object):
    def intersection(self, nums1, nums2):
        sa = set(nums1)
        res = []
        for elem in nums2:
            if elem in sa:
                res.append(elem)
                sa.remove(elem)
        return res
        