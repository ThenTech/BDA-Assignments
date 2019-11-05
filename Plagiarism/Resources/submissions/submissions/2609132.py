db = int(input())
mb = int(input())
yb = int(input())
cd = int(input())
cm = int(input())
cy = int(input())
age = 0
if cy - yb > 0:
    if cm - mb > 0:
        age += cm-mb
    elif cm - mb == 0:
        if cd - db > 0:
            age += cd -db
    else:
        age +=cd-db+1
elif cy - yb == 0:
    if cm - mb > 0:
        age += cm-mb
    elif cm - mb == 0:
        if cd - db > 0:
            age += cd -db
print(age)