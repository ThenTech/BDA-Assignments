db = int(input())
mb = int(input())
yb = int(input())
cd = int(input())
cm = int(input())
cy = int(input())
age = 0
if cy - yb  > 0:
    if cm -mb > 0:
        age += cy-yb
    elif cm -mb == 0:
        if cd-db >= 0:
            age += cy-yb
    else:
        age += cy -yb -1
elif cy -yb ==0:
    if cm -mb > 0:
        if cm -mb > 0:
            age += cy-yb
    elif cm -mb == 0 :
        if cd-db >= 0:
            age += cy-yb
print(age)