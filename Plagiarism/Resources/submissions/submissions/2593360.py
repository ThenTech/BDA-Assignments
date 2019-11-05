def lister():
    list = []
    for i in input():
        if i in '0123456789':
            list += i
    return list

def subsets(input):
    subsethelper(input, [])
    
    
def printer(list):
    for i in list:
        print(i, end=' ')

def subsethelper(left, instring)
    printer(instring)
    if len(left) == 0:
        return
    subsethelper(left[1:], instring+left[0])
    subsethelper(left[1:], instring)





subsets(lister())