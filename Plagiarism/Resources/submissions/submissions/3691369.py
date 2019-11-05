cent = int(input())

euro2 = cent // 200
euro = (cent-200*euro2) // 100
cent50 = (cent-200*euro2-100*euro) // 50
cent20 = (cent-200*euro2-100*euro-cent50*50) // 20
cent10 = (cent-200*euro2-100*euro-cent50*50-cent20*20) // 10
cent5 = (cent-200*euro2-100*euro-cent50*50-cent20*20-cent10*10) // 5
cent2 = (cent-200*euro2-100*euro-cent50*50-cent20*20-cent10*10-cent5*5) // 2
cent1 = (cent-200*euro2-100*euro-cent50*50-cent20*20-cent10*10-cent5*5-cent2*2)

print("2-euros: " + str(euro2))
print("1-euros: " + str(euro))
print("50c-euros: " + str(cent50))
print("20c-euros: " + str(cent20))
print("10c-euros: " + str(cent10))
print("5c-euros: " + str(cent5))
print("2c-euros: " + str(cent2))
print("1c-euros: " + str(cent1))