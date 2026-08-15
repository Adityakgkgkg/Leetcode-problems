
class Solution(object):
    def searchMatrix(self, matrix, target):
        n ,m = len(matrix), len(matrix[0])
        low , high = 0 , (n * m) - 1
        while low <=high:
            mid = (low + high) // 2
            i = mid // m
            j = mid % m
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                high = mid - 1
            else:
                low = mid + 1
        return False