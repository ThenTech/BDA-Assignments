input1 = input('How much do you have?')
input1 = int(input1)
euros2 = input1//200
euros1 = (input1-(euros2*200))//100
cent50 = (input1 -(euros2*200)-(euros1*100))//50
cent20 = (input1 -(euros2*200)-(euros1*100)-(cent50*50))//20
cent10 = (input1 -(euros2*200)-(euros1*100)-(cent50*50)-(cent20*20))//10
cent5 = (input1 -(euros2*200)-(euros1*100)-(cent50*50)-(cent20*20)-(cent10*10))//5
cent2 = (input1 -(euros2*200)-(euros1*100)-(cent50*50)-(cent20*20)-(cent10*10)-(cent5*5))//2
cent1 = (input1 -(euros2*200)-(euros1*100)-(cent50*50)-(cent20*20)-(cent10*10)-(cent5*5)-(cent2*2))//1

print('2-euros:', euros2)
print('1-euros:', euros1)
print('50c-euros:', cent50)
print('20c-euros:', cent20)
print('10c-euros:', cent10)
print('5c-euros:', cent5)
print('2c-euros:', cent2)
print('1c-euros:', cent1)
