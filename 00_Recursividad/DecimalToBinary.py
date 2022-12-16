
def Dec2Bin(n):
    assert int(n) == n and n > 0, 'The numbers must be a positive integer'
    if n in [0,1]:
        return n
    else:
        return n%2 + 10*Dec2Bin(n//2)

print(Dec2Bin(48))
         

