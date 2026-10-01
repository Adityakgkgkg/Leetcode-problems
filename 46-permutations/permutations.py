class Solution(object):
    def permute(self, nums):
        ans = []
        path =[]
        used = [False] * len(nums)
        def backtrack():
            for i in range(len(nums)):
                if len(path) ==len(nums):
                    ans.append(path[:])
                    return
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack()
                    path.pop()
                    used[i] = False
        backtrack()
        return ans

        