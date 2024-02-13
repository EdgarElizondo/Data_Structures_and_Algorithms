

def stringToAnotherTD(string1,string2,dp = {}):
    if string1 == "": 
        return len(string2)
    elif string2 == "": 
        return len(string1)
    elif string1[0] == string2[0]:
        return stringToAnotherTD(string1[1:],string2[1:],dp)
    elif string1+string2 in dp: return dp[string1+string2]
    deleteOp = 1 + stringToAnotherTD(string1,string2[1:],dp)
    insertOp = 1 + stringToAnotherTD(string1[1:],string2,dp)
    changeOp = 1 + stringToAnotherTD(string1[1:],string2[1:],dp)
    
    dp[string1+string2] = min(deleteOp,insertOp,changeOp)
    return dp[string1+string2]


def stringToAnotherDT(text1,text2):
    minChanges = [0]*min(len(text1),len(text2)) + [1]*abs(len(text1)-len(text2))
    for i in range(min(len(text1),len(text2))-1,-1,-1):
        op1 = 1 + minChanges[i+1]
        op2 = 1 + minChanges[i-1]
        op3 = 0
        minChanges[i] = min(op1,op2,op3)
    return minChanges[0]

text1 = "table"
text2 = "tbrltt"
print(stringToAnotherTD(text1,text2))
print(stringToAnotherDT(text1,text2))
