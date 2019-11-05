def merge_lists(list1, list2):
    if not len(list1) <= len(list2):
        list3 = list2[:]
        list2 = list1[:]
        list1 = list3[:]
    

    mergedlist = []
    l1_counter = 0
    l2_counter = 1

    while l1_counter < len(list1) and l_2counter < len(list2):
        if list1[l1_counter] < list2[l2_counter]:
            mergedlist.append[l1_counter]
            l1_counter += 1
        else:
            mergedlist.append[l2_counter]
            l2_counter += 1
    
    if l2_counter < len(list2) - 1:        
        for item in list2[l2_counter:]:
            mergedlist.append(item)
    if l1_counter < len(list1) - 1:        
        for item in list1[l1_counter:]:
            mergedlist.append(item)

        

def merge_sort(l):
    if len(l) <= 1:
        return l
    if len(l) == 2:
        l = l.sort()
        return l
    else:
        half = (len(l)//2) - 1
        first_half = merge_sort(l[:half])
        second_half = merge_sort(l[half:])
        return merge_lists(first_half, second_half)
        
        
    
