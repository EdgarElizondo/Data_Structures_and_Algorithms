
def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer'
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
         
fact = factorial(5)
print(fact)