# write your code here

def sub(subsets, to_do):
    returnlist = subsets[:]
    
    if len(to_do) >= 1:
        for item in range(len(subsets)):
            returnlist.append(subsets[item] + to_do[0])
        
        returnlist = sub(returnlist, to_do[1:])
        return returnlist
    
    else:
        return returnlist



def gen_subsets(wholeset):
    list = []
    list.append('')
    list.append(wholeset[0])
    sub(list, wholeset[1:])



wholeset = input('please enter the input: ')
wholeset = wholeset.split(' ')
gen_subsets(wholeset)