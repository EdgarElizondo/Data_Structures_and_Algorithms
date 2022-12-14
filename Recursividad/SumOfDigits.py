
def SumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer'
    if n in list(range(10)):
        return n
    else:
        return n%10 + SumOfDigits(n//10)
         
print(SumOfDigits(18562))