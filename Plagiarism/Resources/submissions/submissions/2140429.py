bd = int(input())
bm = int(input())
by = int(input())

td = int(input())
th = int(input())
ty = int(input())

age = ty - by

if bm < tm:
    print(age -1)
elif bm == tm:
    if bd <= td:
        print(age - 1)        
    else:
        print(age)
else:
    print(age)