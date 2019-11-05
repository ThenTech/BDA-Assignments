amount=int(input("amount of money in eurocent: "))
euro2=amount//200
euro1=(amount-euro2*200)//100
eurocent50=(amount-(euro1*100+euro2*200))//50
eurocent20=(amount-(eurocent50*50+euro1*100+euro2*200))//20
eurocent10=(amount-(eurocent20*20+eurocent50*50+euro1*100+euro2*200))//10
eurocent5=(amount-(eurocent10*10+eurocent20*20+eurocent50*50+euro1*100+euro2*200))//5
eurocent2=(amount-(eurocent5*5+eurocent10*10+eurocent20*20+eurocent50*50+euro1*100+euro2*200))//2
eurocent1=(amount-(eurocent2*2+eurocent5*5+eurocent10*10+eurocent20*20+eurocent50*50+euro1*100+euro2*200))//1
print("2-euros:",euro2)
print("1-euros:",euro1)
print("50c-euros:",eurocent50)
print("20c-euros:",eurocent20)
print("10c-euros:",eurocent10)
print("5c-euros:",eurocent5)
print("2c-euros:",eurocent2)
print("1c-euros:",eurocent1)