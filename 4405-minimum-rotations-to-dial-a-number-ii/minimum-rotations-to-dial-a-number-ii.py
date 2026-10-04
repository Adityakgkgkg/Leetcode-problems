class Solution(object):
    def minRotations(self, n, s):

        def dist(a, b):
            diff = abs(a - b)
            return min(diff, 10 - diff)

        normal_cost = dist(0, int(s[0]))

        for i in range(1, n):
            normal_cost += dist(int(s[i-1]), int(s[i]))

        answer = normal_cost

        # k = 0
        reverse_all = normal_cost - dist(0, int(s[0])) + dist(0, int(s[n-1]))
        answer = min(answer, reverse_all)

        # k > 0
        for k in range(1, n):
            old = dist(int(s[k-1]), int(s[k]))
            new = dist(int(s[k-1]), int(s[n-1]))

            candidate = normal_cost - old + new

            answer = min(answer, candidate)

        return answer
        