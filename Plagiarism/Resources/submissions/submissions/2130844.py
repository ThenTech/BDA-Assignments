Value=input("How many coins of 1 eurocents do you have?")
Value2=input("How many coins of 2 eurocents do you have?")
Value3=input("How many coins of 5 eurocents do you have?")
Value4=input("How many coins of 10 eurocents do you have?")
Value5=input("How many coins of 20 eurocents do you have?")

Eurocents=(int(Value)*1)+(int(Value2)*2)+(int(Value3)*5)+(int(Value4)*10)+(int(Value5)*20)

Euro=(int(Eurocents)/100)
C10=(Euro%100)//10
C1=Euro%10

print("You have",int(Euro),".", int(C10),int(C1),"euro!")