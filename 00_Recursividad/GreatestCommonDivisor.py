
def GCD(num0,num1):
    assert int(num0) == num0 and int(num1) == num1, 'The numbers must be a integer'
    num0 = abs(num0)
    num1 = abs(num1)
    maxVal = max(num0,num1)
    minVal = min(num0,num1)
    if maxVal%minVal == 0:
        return minVal
    else:
        return GCD(minVal,maxVal % minVal)
         
print(GCD(48,24))