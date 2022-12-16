
def Dec2Bin(n):
    assert int(n) == n and n > 0, 'The numbers must be a positive integer'
    if n in [0,1]:
        return 0
    else:
        return n%2 + 10*Dec2Bin(n//2)
         

def stringifyNumbers(obj):
    # TODO
    lst = {}
    for ind in obj:
        print(type(obj[ind]))
        if (type(obj[ind]) is dict)|(type(obj[ind]) is list):
            lst[ind] = stringifyNumbers(obj[ind])
        elif type(obj[ind]) is int:
            lst[ind] = str(obj[ind])
        else:
            lst[ind] = obj[ind]
    return lst

obj = { "num": 1,
        "test": [],
        "data": {"val": 4,
                "info": {"isRight": True,
                        "random": 66
                        }
                }
        }
print(stringifyNumbers(obj))

print(type(obj['num']))