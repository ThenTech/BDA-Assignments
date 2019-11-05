# write your code here
x=input()
uitkomst=1
som=0
teller=1
for teller in range(1,int(x)+1):
    uitkomst= uitkomst*teller
    teller+=1
    som+= uitkomst
print(som)