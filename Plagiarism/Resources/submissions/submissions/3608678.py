# write your code here

n = int(input())
m = int(input())

def recur(list, m, result):
    if len(result) == m:
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
    for i in range(n):
        list.append(i)
    recur(list, m, "")

make_list(n, m)