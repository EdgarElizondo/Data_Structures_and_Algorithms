import math

#________________________________________________________________________
# Bubble Sorting ________________________________________________________
def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
#________________________________________________________________________
# Selection Sorting ________________________________________________________
def selectionSort(array):
    for i in range(len(array) - 1):
        minInd = i
        for j in range(i + 1,len(array)):
            if array[j] < array[minInd]:
                minInd = j
        array[i], array[minInd] = array[minInd], array[i]
    return array
#________________________________________________________________________
# Insertion Sorting ________________________________________________________
def insertionSort(array):
    for i in range(1,len(array)):
        j = i -1
        key = arr[i]
        while (j >=  0) & (key < array[j]):
            array[j + 1] = array[j]
            j -= 1
        arr[j + 1] = key
    return array
#________________________________________________________________________
# Bucket Sorting ________________________________________________________
def bucketSort(array):
    arr = []
    maxValue = max(array)
    nbuckets = round(math.sqrt(len(array)))
    # Creating each bucket
    for i in range(nbuckets):
        arr.append([])
    # Assingned a bucket to each element
    for i in range(len(array)):
        bucket = math.ceil(array[i]*nbuckets/maxValue)
        arr[bucket - 1].append(array[i])
    # Last sorting
    for i in range(nbuckets):
        arr[i] = bubbleSort(arr[i])        
    # Merging buckets
    k = 0
    for i in range(nbuckets):
        for j in range(len(arr[i])):
            array[k] = arr[i][j]
            k += 1
    return array
#________________________________________________________________________
# Merge Sorting ________________________________________________________
def merge(array,left,middle,right):
    div0 =  middle - left + 1
    div1 = right - middle

    L = [0] * div0
    for i in range(div0):
        L[i] = array[left + i]

    R = [0] * div1
    for i in range(div1):
        R[i] = array[i + middle + 1]
    
    i = 0
    j = 0
    k = left
    # Merging the arrays
    while (i < div0) | (j < div1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    # 
    while (i < div0):
        array[k] = L[i]
        i += 1
        k += 1
    while (j < div1):
        array[k] = R[j]
        j += 1
        k += 1



def mergeSort(array,left = 0, right = None):
    if right == None:
        right = len(array) - 1
    if left < right:
        middle = (left + (right - 1))//2 
        mergeSort(array,left,middle)
        mergeSort(array,middle + 1,right)
        merge(array,left,middle,right)

    return array

arr = [2,1,7,6,5,3,4,9,8]
arr = mergeSort(arr)
print(arr)
