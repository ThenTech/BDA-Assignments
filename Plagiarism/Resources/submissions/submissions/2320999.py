numero=input("numero: ")

pares=0

for i in numero:
    if int(i)%2==0:
        pares +=1

print(pares)