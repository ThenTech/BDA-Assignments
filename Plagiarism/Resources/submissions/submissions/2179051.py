total_euro = int(input("How many euro?"))

euro2 = total_euro//200
total_euro = total_euro - euro2*200
euro1 = total_euro//100
total_euro = total_euro - euro1*100
cent50 = total_euro//50
total_euro = total_euro - cent50*50
cent20 = total_euro//20
total_euro = total_euro - cent20*20
cent10 = total_euro//10
total_euro = total_euro - cent10*10
cent5 =  total_euro//5
total_euro = total_euro - cent5*5
cent2 = total_euro//2
total_euro = total_euro - cent2*2
cent1 = total_euro

print("2-euros:", euro2)
print("1-euros:", euro1)
print("50c-euros:", cent50)
print("20c-euros:", cent20)
print("10c-euros:", cent10)
print("5c-euros:", cent5)
print("2c-euros:", cent2)
print("1c-euros:", cent1)