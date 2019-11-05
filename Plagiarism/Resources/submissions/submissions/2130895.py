x=input()
som=1
teller=2
vorige=1
fractaal=0
for value in range(int(x)-1):
    fractaal= teller*vorige
    vorige=fractaal
    teller+=1
print(fractaal)