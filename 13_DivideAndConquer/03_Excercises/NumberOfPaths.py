

def numberOfPaths(matrix,value, row = 0,col = 0):
    size = len(matrix) - 1
    if value < 0:
        return 0
    elif (row == size) & (col == size) & (value == 0):
        return 1
    elif (row == size) & (col == size) & (value != 0):
        return 0
    elif (row == size):
        return numberOfPaths(matrix,value-matrix[row][col],row,col+1)
    elif (col == size):
        return numberOfPaths(matrix,value-matrix[row][col],row+1,col)
    opt1 = numberOfPaths(matrix,value-matrix[row][col],row,col+1)
    opt2 = numberOfPaths(matrix,value-matrix[row][col],row+1,col)
    return opt1 + opt2


value = 28
matrix = [[4,7,1,6],[5,7,3,9],[3,2,1,2],[7,1,6,3]]
result = numberOfPaths(matrix,value)
print(result)