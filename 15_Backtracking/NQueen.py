
class NQueens:
    def __init__(self,n):
        self.n = n
        self.chess = [[0 for i in range(n)] for j in range(n)]
    
    def __str__(self):
        text = ""
        for i in range(self.n):
            for j in range(self.n):
                text += str(self.chess[i][j]) + "  "
            text += "\n"
        return text

    def isSafe(self,row,col):
        #Check for any queen in the same row or column
        for i in range(self.n):
            if (self.chess[i][col] == 1): return False
        #Check for any queen in the same diagonal
        for i in range(row+1):
            if (row - i < 0) | (col - i < 0): break
            if self.chess[row-i][col-i] == 1: return False
        for i in range(row+1):    
            if (row - i < 0) | (col + i >= self.n): break
            if self.chess[row-i][col+i] == 1: return False
        return True

    def solve(self,row = 0):
        if row == self.n: return True
        for col in range(self.n):
            if self.isSafe(row,col):
                self.chess[row][col] = 1
                if self.solve(row+1):
                    return True
            self.chess[row][col] = 0
        return False
    
    def solveQueens(self):
        if self.solve(): print(self)
        else: print("There is not solution")

queens= NQueens(10)
queens.solveQueens()
