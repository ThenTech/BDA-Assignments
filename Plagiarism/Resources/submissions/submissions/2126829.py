c1 = float(input("Please enter the amount of 1 cent coins you have: "))
c2 = float(input("Please enter the amount of 2 cent coins you have: "))
c5 = float(input("Please enter the amount of 5 cent coins you have: "))
c10 = float(input("Please enter the amount of 10 cent coins you have: "))
c20 = float(input("Please enter the amount of 20 cent coins you have: "))

money = (c1 + (c2*2) + (c5*5) + (c10*10) + (c20*20))/100
print ("you have ", money, "euros!")