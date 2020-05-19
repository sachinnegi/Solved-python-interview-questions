#time complexity = N! (because of N^N arrangements)

class Solution:
    def totalNQueens(self, n: int) -> int:
        dia_diff = set()            # y-x = c     (45 deg angle)
        dia_sum = set()             # it uses y=mx+c -> y=-x+c -> y+x = c (135 degree angle)
        col_used = set()
        return self.helper(dia_diff,dia_sum,col_used,n,0)
    
    def isSafe(self, dia_diff, dia_sum, col_used, col, n, row):
        if (col+row not in dia_sum and row-col not in dia_diff and col not in col_used):
            return True
        return False
    
    def helper(self, dia_diff, dia_sum, col_used, n, row):
        if row == n:        #found a solution
            return 1
        
        solution = 0
        
        for col in range(n):   # check each col for current row
            # if the current col is safe
            if self.isSafe(dia_diff, dia_sum, col_used, col, n, row):
                
                dia_diff.add(row-col)
                dia_sum.add(row+col)
                col_used.add(col)
                #choose and explore
                solution += self.helper(dia_diff, dia_sum, col_used, n, row+1)  # check for other row
                
                #unchoose
                dia_diff.remove(row-col)
                dia_sum.remove(row+col)
                col_used.remove(col)
        return solution
