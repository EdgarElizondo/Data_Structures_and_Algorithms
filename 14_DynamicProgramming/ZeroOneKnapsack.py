
class Item:
    def __init__(self,weight,value,name):
        self.weight = weight
        self.value = value
        self.ratio = value/weight
        self.name = name

def zeroOneKnapsackTD(capacity,arr,dp = {}):
    if (capacity <= 0) | (len(arr) < 1): return 0
    elif (capacity < arr[0].weight): return 0
    dictKey = arr[0].name + str(capacity)
    if dictKey in dp: return dp[dictKey]

    profit1 = arr[0].value + zeroOneKnapsackTD(capacity - arr[0].weight,arr[1:],dp)
    profit2 = zeroOneKnapsackTD(capacity,arr[1:],dp)
    dp[dictKey] = max(profit1,profit2)
    print(dp)
    return dp[dictKey]

mango = Item(3,31,"mango")
apple = Item(1,26,"apple")
orange = Item(2,17,"orange")
banana = Item(5,72,"banana")
capacity =  7
listFuits = [mango,apple,orange,banana]
print(zeroOneKnapsackTD(capacity,listFuits))
#print(zeroOneKnapsackDT(capacity,listFuits))
