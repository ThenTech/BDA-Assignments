# write your code here
x=input()
uitkomst=1
som=0
teller=1
teller_2=1
for teller_2 in range(1,int(x)):
    for teller in range(1,teller_2):
        uitkomst = uitkomst*teller
        teller+=1
    som+=uitkomst
    teller_2+=1
print(uitkomst)