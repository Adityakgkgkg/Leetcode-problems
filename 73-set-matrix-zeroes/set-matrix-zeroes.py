class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        # Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True

        # Check first column
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set marked rows to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Set marked columns to zero
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Finally handle first row
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        # Finally handle first column
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
    
        