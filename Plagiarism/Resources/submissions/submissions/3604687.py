def is_unique(li1):
    li2 = []
    for i in range(len(li1)):
        for j in range(len(li2)):
            if(li1[i] == li2[j]):
                return False
        li2.append(li1[i])
    return True