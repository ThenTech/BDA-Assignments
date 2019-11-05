def coll(m, n, li):
    if (len(li) == n):
        printLi(li)
    else:
        for i in range(m):
            first = m-i
            new_li = li + [first]
            coll(m-1-i, n, new_li)


def printLi(li):
     for element in li:
         print(element, end=" ")
     print()

def help_coll():
     m = int(input())
     n = int(input())
     coll(m,n, [])

help_coll()