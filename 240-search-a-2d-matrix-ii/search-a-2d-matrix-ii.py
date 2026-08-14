class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m - 1
        for i in range(n):
            for j in range(m):
                if target > matrix[i][j]:
                    i +1
                elif target < matrix[i][j]:
                    j -1
                else:
                    return True
        return False
        