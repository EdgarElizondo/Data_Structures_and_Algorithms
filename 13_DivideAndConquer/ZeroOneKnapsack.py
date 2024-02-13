

class Item:
    def __init__(self,weight,value,name):
        self.weight = weight
        self.value = value
        self.ratio = value/weight
        self.name = name

def zeroOneKnapsack(capacity,arr):
    if (capacity <= 0) | (len(arr) < 1):
        return 0
    elif (capacity < arr[0].weight):
        return 0
    else:
        profit1 = arr[0].value + zeroOneKnapsack(capacity - arr[0].weight,arr[1:])
        profit2 = zeroOneKnapsack(capacity,arr[1:])
        return max(profit1,profit2)
    
    
mango = Item(3,31,"mango")
apple = Item(1,26,"apple")
orange = Item(2,17,"orange")
banana = Item(5,72,"banana")
capacity =  7
listFuits = [mango,apple,orange,banana]
result =  zeroOneKnapsack(capacity,listFuits)
print(result)
