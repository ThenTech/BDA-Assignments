n = int(input())
m = int(input())

def recur(list, m, result):
    if 0 == m:
        print(result)
        return
    if len(list) == 0:
        return
    for i in list:
        buffer = result + str(i)
        buffer += " "
        del list[0]
        recur(list, m-1, buffer)
        recur(list, m, result)

def make_list(n, m):
    list = []
    for i in range(1, n+1):
        list.append(i)
    recur(list, m, "")

make_list(n, m)