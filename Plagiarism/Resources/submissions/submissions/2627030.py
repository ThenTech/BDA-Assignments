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
    if len(wholeset) == 0:
        return []
    if len(wholeset) == 1:
        return [wholeset[0], '']
    list = []
    list.append('')
    list.append(wholeset[0])
    return sub(list, wholeset[1:])
    



wholeset = input('please enter the input: ')
wholeset = wholeset.split(' ')
output = gen_subsets(wholeset)

for item in output:
    if len(item) == 0:
        print()
    else:
        for char in range(len(item)):
            if not char == len(item)-1:
                print(item[char] + ' ', end='')
            else:
                print(item[char])

