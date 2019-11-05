c1 = int(input("1"))
c2 = int(input("1"))
c5 = int(input("1"))
c10 = int(input("1"))
c20 = int(input("1"))

total = (c1 + c2*2 + c5*5 + c10*10 + c20*20)
euro = int(total/100)
cent10 = int((total - (euro*100))/ 10)
cent1 = int(total - (euro*100) - cent10)


print("You have ", euro, ".", cent10, cent1, " euro!", sep="")