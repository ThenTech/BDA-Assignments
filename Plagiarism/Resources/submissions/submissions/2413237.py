def merge_lists(first, second):
    i = 0
    result = []
    if len(second) < len(first):
        placeholder = second[:]
        second = first[:]
        first = placeholder[:]
    
    
    while len(first) >= 1 and len(second) >= 1:
        if first[0] < second[0]:
            result.append(first[0])
            del first[0]
            if len(first) == 0:
                result += second[:]
        else:
            result.append(second[0])
            del second[0]
            if len(second) == 0:
                result += first[:]
                
            
    return result   


def merge_sort(l):
    if n>1:
        list1 = merge_sort(l[:len(l)//2])
        list2 = merge_sort(l[len(l)//2:])
        return (merge_lists(list1, list2))
    else:
        return l
        
        

