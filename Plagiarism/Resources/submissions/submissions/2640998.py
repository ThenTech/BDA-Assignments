def counter(list, number):
    count = 0
    for getal in list:
        if getal == number:
            count += 1
    return count

def is_unique(l):
    for i in range(len(l)):
        if counter(l, l[i]) != 1:
            return False
    return True