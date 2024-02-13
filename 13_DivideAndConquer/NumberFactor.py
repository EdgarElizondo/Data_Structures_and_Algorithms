

def numberFactorPermutations(n):
    # factors = [1,3,4]
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numberFactorPermutations(n-1)
        subP2 = numberFactorPermutations(n-3)
        subP3 = numberFactorPermutations(n-4)
        return (subP1 + subP2 + subP3)

def numberFactorCombinations(n):
    subP = 0
    factors = [1,3,4]
    if n == 0: return 1
    for num in factors:
        if n >= num:
            subP += numberFactorCombinations(n-num)
    return subP


n = 8
res = numberFactorCombinations(n)
print(res)