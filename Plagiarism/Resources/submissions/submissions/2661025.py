def is_unique(str):
    l = []
    for char in str:
        if char in l:
            return False
        else:
            l.append(char)
    return True

def collection_helper(length, possibles, prefix):
    if len(prefix) == length:
        if is_unique(prefix):
            for arg in prefix:
                print(arg, end=" ")
            print()
    else:
        for pos in possibles:
            collection_helper(length, possibles, prefix + str(pos))

def collect(pos, length):
    l = []
    t = []
    for i in range(1, pos + 1):
        l.append(i)
    collection_helper(length, l, "")

collect(input(), input())