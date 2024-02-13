
def houseRobber(arr):
    if len(arr) == 0:
        return 0
    else:
        subP1 = arr[0] + houseRobber(arr[2:])
        subP2 = houseRobber(arr[1:])
        return max(subP1,subP2)


houses = [6,7,1,30,8,2,4]
res = houseRobber(houses)
print(res)