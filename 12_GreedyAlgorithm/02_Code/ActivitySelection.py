

def maxActivities(arr):
    arr.sort(key = lambda x:[x[2]])
    count = 1
    lastActivity = arr[0][2]
    for i in range(1,len(arr)):
        if arr[i][1] >= lastActivity:
            lastActivity = arr[i][2]
            count += 1
    return count

activities = [["A1",0,6],
              ["A2",3,4],
              ["A3",1,2],
              ["A4",5,8],
              ["A5",5,7],
              ["A6",8,9]]

numActivities = maxActivities(activities)
print(numActivities)