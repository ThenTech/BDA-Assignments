def lijstfunc(lijst):
    x = 0
    for l in range(0, len(lijst)):
        lijst = lijst[:] + l[x]
        x += 1
    if l[y] < l[y+1]:
        return True
    elif l[y+1] == "":
        return True
    else:
        return False
y = 0
l = 0
lijst = input()