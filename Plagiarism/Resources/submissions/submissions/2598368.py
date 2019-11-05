s1 = int(input("1"))
s2 = int(input("2"))
s5 = int(input("5"))
s10 = int(input("10"))
s20 = int(input("20"))

total = s1 + (s2*2) + (s5*5) + (s10*10) + (s20*20)

euro1 = total//100
euro2 = (total - (euro1*100))//10
euro3 = (total - (euro1*100) - (euro2*10))

print("You have ", euro1,".", euro2, euro3, " euro!", sep="")
