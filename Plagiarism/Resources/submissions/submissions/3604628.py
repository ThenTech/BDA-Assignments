def is_ordered(li):
    for i in range(1, len(li)):
        if (li[i-1] > li[i]):
            return False
    return True