class Solution(object):
    def minSwaps(self, nums):
        def digit_sum(num):
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            return total

        n = len(nums)

        arr = sorted(
            [(digit_sum(x), x, i) for i, x in enumerate(nums)]
        )

        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            ans += cycle_size - 1

        return ans
        