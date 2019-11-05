l=1
def is_ordered(l):
    for x in l-1:
        if l[x] > l[x-1]:
            return False
        else:
            return True
print(is_ordered(l))