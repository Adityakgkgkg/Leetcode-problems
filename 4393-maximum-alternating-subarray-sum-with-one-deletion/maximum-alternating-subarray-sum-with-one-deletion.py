class Solution(object):
    def maxAlternatingSum(self, nums):
        pos0 = nums[0]
        neg0 = float('-inf')

      
        pos1 = float('-inf')
        neg1 = float('-inf')

        answer = nums[0]

        for x in nums[1:]:
            old_pos0 = pos0
            old_neg0 = neg0
            old_pos1 = pos1
            old_neg1 = neg1

      
            pos0 = max(x, old_neg0 + x)
            neg0 = old_pos0 - x

            
            pos1 = max(old_pos0, old_neg1 + x)
            neg1 = max(old_neg0, old_pos1 - x)

            answer = max(answer, pos0, neg0, pos1, neg1)

        return answer   