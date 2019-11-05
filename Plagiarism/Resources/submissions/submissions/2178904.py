cent1 = int(input("1 cents?"))
cent2 = int(input("2 cents?"))
cent5 = int(input("5 cents?"))
cent10 = int(input("10 cents?"))
cent20 = int(input("20 cents?"))





sum = 20*cent20 + 10*cent10 + 5*cent5 + 2*cent2 + 1*cent1
euro1 = sum//100
euro2 = (sum - euro1*100)//10
euro3 = (sum - euro1*100 - euro2*10)//1

print("You have ", euro1,".", euro2, euro3, " euro!", sep="")