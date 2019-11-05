# write your code here
totaal=int(input())
euros= totaal //100
E2= euros//2
E1= euros - E2*2

tientallen= (totaal % 100)
tientallen2= int(tientallen /10)
c50= tientallen2//5
c20= (tientallen2-c50*5)//2
c10= tientallen2 -c50*5-c20*2

centen= tientallen % 10
c5= centen//5
c2= (centen-c5*5)//2
c1= centen -c5*5-c2*2

print("2-euros:",E2)
print("1-euros:",E1)
print("50c-euros:",c50)
print("20c-euros:",c20)
print("10c-euros:",c10)
print("5c-euros:",c5)
print("2c-euros:",c2)
print("1c-euros:",c1)