

class Item:
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value
        self.density = value/weight

def maxValueBox(capacity,listItem):
    weight = 0
    maxValue = 0
    listItem.sort(key = lambda x: x.density ,reverse = True)

    for item in listItem:
        print(maxValue)
        if capacity >= weight + item.weight:
            weight += item.weight
            maxValue += item.value
        else:
            fraction = (capacity-weight)/item.weight
            maxValue += item.value*fraction
            return maxValue 
    return maxValue

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
listItem = [item1,item2,item3]
box = 50
res = maxValueBox(box,listItem)
print(res)