

def minChange(n,arr):
    ind = 0
    count = 0
    arr.sort(reverse = True)
    while n > 0:
        if n - arr[ind] >= 0:
            count += 1
            n -= arr[ind]
        else:
            ind += 1
    return count

change = [1,2,5,10,20,50,100,200,500,1000]
amount = 301
res = minChange(amount,change)
print(res)