def is_unique(list):
    for i in range(len(list)):
        for j in range((i + 1),len(lijst)):
            if list[i] == list[j]:
                return False
    return True