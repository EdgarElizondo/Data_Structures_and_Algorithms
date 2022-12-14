
def Power(base,exp):
    assert int(exp) == exp, 'The number must be a positive integer'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * Power(base,exp + 1)
    else:
        return base * Power(base,exp - 1)
         
print(Power(3,-6))