def lister():
    list = []
    for i in input():
        if i in '0123456789':
            list += i
    return list

def subsets(input):
    subsethelper(input, [])
    
    
def printer(list):
    print(list[0])
    for i in list[1:]:
        print(' ',i, sep='')
    print()

def subsethelper(left, instring):
    printer(instring)
    if len(left) == 0:
        return
    subsethelper(left[1:], instring+[left[0]])
    subsethelper(left[1:], instring)





subsets(lister())