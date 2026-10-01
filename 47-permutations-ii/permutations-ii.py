class Solution(object):
    def permuteUnique(self, nums):
        ans =[]
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(nums) ==len(path):
                ans.append(path[:])
                return 
            seen = set()
            for i in range(len(nums)):
                if used[i]:
                    continue
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                used[i] = True
                path.append(nums[i])

                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return ans
