x=int(input("geef getal"))
product=1
som=0
for j in range(1,x+1)
    for i in range(1,j+1):
        product=product*(j-i+1)
    som=som+product
print(som)