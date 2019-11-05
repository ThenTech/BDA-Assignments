# write your code here
a = int(input('Muntstukken 1 cent'))
b = int(input('Muntstukken 2 cent'))
c = int(input('Muntstukken 5 cent'))
d = int(input('Muntstukken 10 cent'))
e = int(input('Muntstukken 20 cent'))
Totaal = a*1 + b*2 + c*5 + d*10 + e*20
euro = Totaal//100
tiencent = (Totaal%100)//10
eurocent = Totaal%10
print("You have ", euro, ".", tiencent, eurocent, " euro!", sep="")