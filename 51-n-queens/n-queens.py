class Solution(object):
    def nQueenUtil(self,j,n,rows,diag1,diag2,path,ans):
        if j > n:
                board = ["."] * n

                for col in range(n):
                    row = path[col] - 1
                    board[row] = "." * col + "Q" + "." * (n - col - 1)

                ans.append(board)
                return
        for i in range(1,n+1):
            if not rows[i] and not diag1[i-j+n] and not diag2[i+j]:
                rows[i] = diag1[i-j+n] = diag2[i+j] = True
                path.append(i)
                
                self.nQueenUtil(j+1, n, rows, diag1, diag2, path, ans)
                    
                rows[i] = diag1[i-j+n] = diag2[i+j] = False
                path.pop()
    def solveNQueens(self, n):
        rows = [False] * (n+1)
        diag1 = [False] * (2*n+1)
        diag2 = [False] * (2*n+1)
        path = []
        ans = []
        
        self.nQueenUtil(1,n,rows,diag1,diag2,path,ans)
            
        return ans
        