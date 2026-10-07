class Solution(object):
    def longestDiverseString(self, a, b, c):
        heap = []

        if a > 0:
            heapq.heappush(heap, (-a, 'a'))

        if b > 0:
            heapq.heappush(heap, (-b, 'b'))

        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        ans = []

        while heap:
            count, ch = heapq.heappop(heap)
            count = -count

            # Cannot use this character
            if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:

                if not heap:
                    break

                count2, ch2 = heapq.heappop(heap)
                count2 = -count2

                ans.append(ch2)
                count2 -= 1

                if count2 > 0:
                    heapq.heappush(heap, (-count2, ch2))

                heapq.heappush(heap, (-count, ch))

            else:
                ans.append(ch)
                count -= 1

                if count > 0:
                    heapq.heappush(heap, (-count, ch))

        return ''.join(ans)
        