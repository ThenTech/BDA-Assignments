def merge_lists(first, second):
    indexfirst = 0
    indexsecond = 0
    lijst = []
    for i in range(len(first)):
        if first[indexfirst] <= second[indexsecond]:
            lijst.append(first[indexfirst])
            indexfirst += 1
        else:
            lijst.append(second[indexsecond])
    return lijst


def merge_sort(list):
    helft1 = (len(list)/2)
    lijst1 = list[:helft1]
    lijst2 = list[helft2:]
    while ordered(lijst1) is False
        for i in range(len(lijst1)):
            if i < len(lijst2):
                if lijst1[i]>lijst1[i+1]:
                    waarde1 = lijst1[i]
                    waarde2 = lijst1[i+1]
                    lijst1[i] = waarde2
                    lijst1[i+1] = waarde1
    while ordered(lijst2) is False
        for i in range(len(lijst2)):
            if i < len(lijst2):
                if lijst2[i]>lijst2[i+1]:
                    waarde1 = lijst2[i]
                    waarde2 = lijst2[i+1]
                    lijst2[i] = waarde2
                    lijst2[i+1] = waarde1
    oplossing = merge_lists(lijst1, lijst2)
    return oplossing
        
def ordered(lijst):
    index = -1
    for element in lijst:
        index+=1
        if index < len(lijst1):
            if not lijst1[index] < lijst1[index+1]
            return False
    return True
        