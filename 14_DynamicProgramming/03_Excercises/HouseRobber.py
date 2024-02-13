
def houseRobberTD(arr, dp = {}):
    if len(arr) == 0: return 0
    elif arr[0] in dp: return dp[arr[0]]
    subP1 = arr[0] + houseRobberTD(arr[2:],dp)
    subP2 = houseRobberTD(arr[1:],dp)
    dp[arr[0]] = max(subP1,subP2)
    return dp[arr[0]]

def houseRobberDT(arr):
    maxValue = [0]*len(arr) + [0,0]
    for i in range(len(arr)-1,-1,-1):
        maxValue[i] = max(arr[i] + maxValue[i+2],maxValue[i+1])
    return maxValue[0]



houses = [6,7,1,30,8,2,4]
print(houseRobberTD(houses))
print(houseRobberDT(houses))