class Solution(object):
    def rotate(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(i +1,n):
                mat[j][i],mat[i][j] = mat[i][j], mat[j][i]
        for row in mat:
            row.reverse()
        