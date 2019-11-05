# write your code here
def DNA(list, length):
    returnlist = []
    DNAlist = ['A', 'C', 'G', 'T']
    
    
    if length >= 1:
        if len(list) == 0:
            for nucleo in DNAlist:
                returnlist.append(nucleo)
        else:
            for item in range(len(list)):
                previous = list[item]
                for nucleo in DNAlist:
                    next = previous + nucleo
                    returnlist.append(next)
        
        returnlist = DNA(returlist, lenth-1)
                    
    
    else:
        return returnlist
    
    

list = []
length = int(input'Please input n: ')
list = DNA(list, length)

for item in list:
    print(item)
    

