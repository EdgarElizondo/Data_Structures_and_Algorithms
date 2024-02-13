
import numpy as np

NumDays = int(input("How many day's Temperature? "))
temp = np.zeros(NumDays)
for i in range(NumDays):
    temp[i] = float(input("What is the day temperature: "))

meanTemp = np.mean(temp)
Above = np.sum(temp > meanTemp)

print(Above)