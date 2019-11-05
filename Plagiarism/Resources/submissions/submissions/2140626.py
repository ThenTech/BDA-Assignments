number = str(input("geef nummer: "))
h=0
i=0
for p in range(len(number)):
    s = str(number)[i]
    if int(s) % 2 ==0:
        h=h+1
    i=i+1
print(h)