
def merge_sort(l):
    if len(l) == 1:
        return l
    x = function(l)
    [i for i in range(1,x+1)]

def function(l):
    x = l[:len(l)//2]
    y = l[len(l)//2:]
    string = ""
    return function2(x,y,string)
    
def function2(x,y,string):
    for i in x:
        for j in y:
            if i < j:
                string += str(i)
                break
            else:
                string += str(j)
    return string