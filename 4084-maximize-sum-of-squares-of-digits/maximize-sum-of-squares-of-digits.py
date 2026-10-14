class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        nines, rem = divmod(sum, 9)

        ans = "9" * nines

        if rem:
            ans += str(rem)

        ans += "0" * (num - len(ans))

        return ans
        