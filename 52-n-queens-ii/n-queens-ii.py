class Solution(object):
    def nQueenUtil(self,j,n,rows,diag1,diag2,):
        if j > n:
            return 1
        count = 0
        for i in range(1,n+1):
            if not rows[i] and not diag1[i-j+n] and not diag2[i+j]:
                rows[i] = diag1[i-j+n] = diag2[i+j] = True
            
                
                count +=self.nQueenUtil(j+1, n, rows, diag1, diag2)
                    
                rows[i] = diag1[i-j+n] = diag2[i+j] = False
                
        return count
                
    def totalNQueens(self, n):
        rows = [False] * (n+1)
        diag1 = [False] * (2*n+1)
        diag2 = [False] * (2*n+1)
        
        
        return self.nQueenUtil(1,n,rows,diag1,diag2)
            
        
        