# write your code here
x= input()
y=input()
teller= 0
uitkomst = 1
for teller in range(0,int(y)):
    uitkomst= uitkomst * (int(x)-teller)/(int(y)-teller)
print(uitkomst)