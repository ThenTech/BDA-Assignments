def quick_sort(l):
    if len(l) <= 1:
        return l
    
    else:
        pivot = len(l)//2
        first_half = []
        second_half = []
        for item in range(len(l)):
            if not item == pivot:
                if l[item] <= l[pivot]:
                    first_half.append(l[item])
                else:
                    second_half.append(l[item])
        
        return(quick_sort(first_half)+[l[pivot]]+quick_sort(second_half))
        
        