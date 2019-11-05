def subset(l,m): 
    subset_helper(l,[],m)
def subset_helper(l,r,m):
    if len(l)==m:
        for j in r:
            print(j,end=" ")
        print()
    else:
        eerste = l[0]
        rest = l[1:]
        subset_helper(rest,r,m)
        subset_helper(rest,r+[eerste],m)

# write your code here
def functie(n, m):
    teller = 1
    list = []
    while teller < n:
        list.append(teller)
        teller += 1
    subset(list,m)
n = int(input())
m = int(input())
functie(n,m)