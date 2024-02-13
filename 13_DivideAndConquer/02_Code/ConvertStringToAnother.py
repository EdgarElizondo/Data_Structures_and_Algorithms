


def convertStringToAnother(s1,s2,ind1 = 0,ind2 = 0):
    if len(s1) == ind1:
        return len(s2) - ind2
    if len(s2) == ind2:
        return len(s1) - ind1
    if s1[ind1] == s2[ind2]:
        return convertStringToAnother(s1,s2,ind1+1,ind2+1)
    else:
        deleteOp = 1 + convertStringToAnother(s1,s2,ind1,ind2+1)
        insertOp = 1 + convertStringToAnother(s1,s2,ind1+1,ind2)
        changeOp = 1 + convertStringToAnother(s1,s2,ind1+1,ind2+1)
        return min(deleteOp,insertOp,changeOp)
    
text1 = "table"
text2 = "tbrlte"
res = convertStringToAnother(text1,text2)
print(res)