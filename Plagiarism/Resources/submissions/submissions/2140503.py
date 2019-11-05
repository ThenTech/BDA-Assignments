# write your code here
x = int(input())
som=1
teller=1
i=1
for i in range(1,x): 
    teller = teller + teller*i
    som = som + teller
    i+=1
print(som)