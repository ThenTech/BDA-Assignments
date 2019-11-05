d1 = int(input())
m1 = int(input())
y1 = int(input())
d2 = int(input())
m2 = int(input())
y2 = int(input())

d = d2-d1
m = m2-m1
y = y2-y1

if d<0:
    m-=1
if m<0:
    y-=1
    
print(y)