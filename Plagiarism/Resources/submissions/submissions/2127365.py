geld = input("Geef een bedrag in eurocent in.")

euro2 = int(geld)//200
tussen = int(geld)-(euro2*200)

euro1 = tussen//100
tussen = tussen-(euro1*100)

euroc50 = tussen// 50
tussen = tussen-(euroc50*50)

euroc20 = tussen//20
tussen = tussen -(euroc20*20)

euroc10 = tussen//10
tussen = tussen -(euroc10*10)

euroc5= tussen//20
tussen = tussen -(euroc20*20)

euroc2 = tussen//2
tussen = tussen -(euroc2*2)

euroc1 = tussen//1

print("2-euros: ", euro2)
print("1-euros: ", euro1)
print("50-cent: ", euroc50)
print("20-cent: ", euroc20)
print("10-cent: ", euroc10)
print("5-cent: ", euroc5)
print("2-cent: ", euroc2)
print("1-cent: ", euroc1)
