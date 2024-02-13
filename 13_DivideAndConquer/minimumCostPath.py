

def minimumCostPath(matrix,row = 0,col = 0):
    size = len(matrix) - 1
    if (row == size) & (col == size):
        return matrix[row][col]
    elif (row == size):
        return matrix[row][col] + minimumCostPath(matrix,row,col+1)
    elif (col == size):
        return matrix[row][col] + minimumCostPath(matrix,row+1,col)
    
    opt1 = matrix[row][col] + minimumCostPath(matrix,row+1,col)
    opt2 = matrix[row][col] + minimumCostPath(matrix,row,col+1)
    return min(opt1,opt2)


matrix = [[4,7,8,6,4],[6,7,3,9,2],[3,8,1,2,4],[7,1,7,3,7],[2,9,8,9,3]]
result = minimumCostPath(matrix)
print(result)