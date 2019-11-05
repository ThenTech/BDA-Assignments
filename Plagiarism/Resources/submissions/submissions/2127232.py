# write your code here
totaal=str(input())
length2= int(len(totaal)-1)
Lletter = int(totaal[length2])
c5= Lletter//5
c2= (Lletter-c5*5)//2
c1= Lletter -c5*5-c2*2
length2=int(len(totaal)-2)
Lletter= int(totaal[length2])
c50= Lletter//5
c20= (Lletter-c50*5)//2
c10= Lletter -c50*5-c20*2
length2= int(len(totaal)-3)
Lletter= int(totaal[length2])
E2= Lletter//2
E1= Lletter - E2*2
print("2-euros:",E2)
print("1-euros:",E1)
print("50c-euros:",c50)
print("20c-euros:",c20)
print("10c-euros:",c10)
print("5c-euros:",c5)
print("2c-euros:",c2)
print("1c-euros:",c1)