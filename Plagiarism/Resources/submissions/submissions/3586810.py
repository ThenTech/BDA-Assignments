x=int(input("geef een getal "))
totaal=0

for i in range(1,x+1):
    sum=1
    for j in range(1,i+1):
        sum*=j
    totaal+=sum

print (totaal)