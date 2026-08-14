class Solution(object):
    def transpose(self, mat):
        m,n =len(mat),len(mat[0])
        res = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = mat[i][j]
        return res
        