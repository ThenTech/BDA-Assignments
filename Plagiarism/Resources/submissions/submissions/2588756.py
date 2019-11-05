def is_unique(list):
    value = True
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j:
                if list[i] == list[j]:
                    value = False
    return value