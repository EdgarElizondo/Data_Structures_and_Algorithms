

def numberFactor(n,factors):
    subP = 0
    #[1,3,4]
    if n == 0: return 1
    for num in factors:
        if n >= num:
            subP += numberFactor(n-num,factors)
    return subP

def numberFactorMemoization(n,factors,dp =  {}):
    subP = 0
    if n == 0: return 1
    elif n in dp: return dp[n]
    for num in factors:
        if n >= num:
            subP += numberFactorMemoization(n-num,factors,dp)
    dp[n] = subP
    return dp[n]

def numberFactorTabulation(n,factors):
    tb = [1] + [0]*n
    for num in factors:
        for i in range(num,n+1):
            tb[i] += tb[i-num]
    return tb[n]

n = 29
factors = [1, 5, 10, 12, 25, 50]
print(numberFactor(n,factors))
print(numberFactorMemoization(n,factors))
print(numberFactorTabulation(n,factors))