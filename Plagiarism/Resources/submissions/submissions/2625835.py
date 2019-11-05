bd = int(input())
bm = int(input())
by = int(input())
cd = int(input())
cm = int(input())
cy = int(input())
if cy > by:
    if cm >= bm:
        if cd > bd:
            print(cy-by)
        else:
            print(cy-by+1)
    else:
        print(cy-by+1)
else:
    print(0)