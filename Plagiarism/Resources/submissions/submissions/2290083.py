def is_unique(l):
    for values in l:
        amount = 0
        for check in l:
            if values == check:
                amount += 1
                if amount > 1:
                    return False
    
    return True