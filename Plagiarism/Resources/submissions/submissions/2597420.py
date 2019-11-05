input1 = input('How many coins of 1 do you have?')
input2 = input('How many coins of 2 do you have?')
input3 = input('How many coins of 5 do you have?')
input4 = input('How many coins of 10 do you have?')
input5 = input('How many coins of 20 do you have?')


totalcoins = (int(input1)*1)+(int(input2)*2)+(int(input3)*5)+(int(input4)*10)+(int(input5)*20) #123
totaleuro = int(totalcoins)//100
totalcents = totalcoins - (totaleuro*100)
if totalcoins == 0:
    print('You have 0.00 euro!')
if totalcoins != 0:
    print("You have ", totaleuro, ".", totalcents, " euro!", sep="")
