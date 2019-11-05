def collection(lst,length, subset):
    if len(subset) == length:
        print(subset[:-1])
        return
    first = lst[0]
    rest = lst[1:]
    collection(rest, length, subset+first+"")
    collection(rest, length, subset)

n = int(input())
m = int(input())

lst = []

for i in range(n, 0, -1):
    lst.append(i)
collection(list, m, "")