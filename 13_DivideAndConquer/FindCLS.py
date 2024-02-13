


def findCLS(string1,string2):
    if (len(string1) == 0) | (len(string2) == 0):
        return 0
    elif string1[0] == string2[0]:
        opt1 = 1 + findCLS(string1[1:],string2[1:])
    else:
        opt1 = 0
    opt2 = findCLS(string1[1:],string2)
    opt3 = findCLS(string1,string2[1:])
    return max(opt1,opt2,opt3)


string1 = "elephant"
string2 = "erepat"
result = findCLS(string1,string2)
print(result)