# write your code here
def subsets(itemlist, sslist):
    returnlist = itemlist[:]
    
    if not len(sslist) == 0:
        for item in range(len(itemlist)):
            for item2 in sslist:
                returnlist.append(itemlist[item] + item2)
    
        return subsets(returnlist, sslist[1:])            
                
    else:
        return returnlist
            
def gen_subsets(setlist):
    sslist = setlist
    itemlist = []
    itemlist.append('') 
    return subsets(itemlist, sslist)
    


set = input('Please enter your set: ')
setlist = set.split(' ')
sets = gen_subsets(setlist)

for item in sets:
    print(item)