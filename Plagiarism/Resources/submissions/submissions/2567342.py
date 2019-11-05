a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

age = f - c
if e < b:
    age -= 1
elif e == b:
    if d < a:
        age -=1

print(age)