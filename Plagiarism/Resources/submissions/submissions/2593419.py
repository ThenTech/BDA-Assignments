def lister(number):
    list = []
    while number < 0:
        list += [number]
        number -= 1
    return list
    

def collection(number, elements):
    collectionhelper(lister(number), [], elements)


def printer(incol):
    for i in incol:
        print(i, end=' ')
    print()
    

def collectionhelper(list, incol, elements):
    if list == []:
        return
    if len(incol) == elements:
        printer(incol)
        return
    collectionhelper(list[1:], incol+[list[0]], elements)
    collectionhelper(list[1:], incol, elements)


collection(input(), input())