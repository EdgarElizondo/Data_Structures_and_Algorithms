


def findLPS(string):
    if len(string) in (0,1):
        return len(string)
    if string[0] == string[-1]:
        return 2 + findLPS(string[1:-1])
    opt1 = findLPS(string[1:])
    opt2 = findLPS(string[:-1])
    return max(opt1,opt2)


string = "AMEEWMEA"
result = findLPS(string)
print(result)