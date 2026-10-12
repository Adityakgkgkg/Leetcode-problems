class Solution(object):
    def minDistance(self, word1, word2):
        dp ={}
        m,n = len(word1),len(word2)
        def solve(i,j):
            if i ==0:
                return j
            if j == 0:
                return i
            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i-1] ==word2[j-1]:
                dp[(i,j)] = solve(i-1,j-1)
            else:
                delete = solve(i-1,j)
                insert = solve(i,j-1)
                replace = solve(i-1,j-1)
                dp[(i,j)] = 1 + min(
                    delete,insert, replace
                    )
            return dp[(i,j)]
        return solve(m, n)

        
        