import math
import numpy as np

class Sudoku:
    def __init__(self,table):
        row,col = table.shape
        if (row ==  col) & (row/np.sqrt(row) % 1 == 0):
            self.size = row
            self.table = table
        else:
            print("It is not possible to build this sudoku")

    def __str__(self):
        text = ""
        for i in range(self.size):
            for j in range(self.size):
                text += str(self.table[i][j]) + " "
            text += "\n"
        return text
    
    def __isGridValid(self,num,row,col):
        gridSize = int(np.sqrt(self.size))
        startRow = int(row//gridSize)
        startCol = int(col//gridSize)
        for i in range(gridSize):
            for j in range(gridSize):
                if self.table[startRow*gridSize+i][startCol*gridSize+j] == num:
                    return False
        return True
    
    def __isValid(self,num,row,col):
        # validate row and column
        for i in range(self.size):
            if (self.table[row][i] == num) | (self.table[i][col] == num) | (not self.__isGridValid(num,row,col)):
                return False
        return True
    def __hasNumber(self,row,col):
        if self.table[row][col] != 0:
            return True
        return False
        
    def __getSolution(self,row = 0,col = 0,n = 0):
        if (row == self.size - 1) & (col == self.size):
            return True
        elif (col == self.size):
            row += 1
            col = 0
        
        if self.__hasNumber(row,col):
            if self.__getSolution(row,col + 1,n):
                return True    
        else:            
            for num in range(1,self.size+1):
                if self.__isValid(num, row, col):
                    self.table[row][col] = num
                    if self.__getSolution(row,col + 1,n+1):
                        return True
                    self.table[row][col] = 0
            return False
    
    def solve(self):
        if self.__getSolution(): print(self)
        else: print("This sudoku does not have solution") 
            


table = np.array([[0,8,0,6,0,0,0,9,0],
                [0,0,0,5,0,0,1,0,0],
                [0,0,4,0,1,8,0,2,0],
                [7,0,0,0,0,0,0,4,0],
                [0,0,0,1,0,0,0,0,0],
                [0,5,0,0,3,9,2,0,0],
                [0,9,0,0,8,2,3,0,0],
                [0,0,5,0,0,0,0,0,9],
                [0,0,0,0,0,6,0,0,0],
                ])
sudoku = Sudoku(table)
sudoku.solve()
