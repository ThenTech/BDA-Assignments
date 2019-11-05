def ss_helper(s, current):
    if len(s) == 0:
        for element in current:
            print(element, end=" ")
        print()
    else:
        head = s[0]
        tail = s[1:]
        excluded = current[:]
        included = current[:] +[head]
        ss_helper(tail, excluded)
        ss_helper(tail, included)
    



def subset(s):
    ss_helper(s,[])


s=[]
for char in input().split():
    s.append(int(char))
subset(s)