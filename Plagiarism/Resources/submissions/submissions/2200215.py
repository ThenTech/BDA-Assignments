x = int(input("enter a number"))
y = int(input("enter another number"))

xfac = 1
yfac = 1
xminyfac = 1

for i in range(x):
    xfac *= (i+1)
    
for i in range(y):
    yfac *= (i+1)

for i in range(x-y):
    xminyfac *= (i+1)

bico = xfac / (yfac*xminyfac)

print(int(bico))