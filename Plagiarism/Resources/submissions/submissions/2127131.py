# write your code here
amount = int(input("How much money has to be paid?"))

euro2 = amount//200
euro1 =(amount-200*euro2)//100
euro50c =(amount-200*euro2-100*euro1)//50
euro20c =(amount-200*euro2-100*euro1-50*euro50c)//20
euro10c =(amount-200*euro2-100*euro1-50*euro50c-20*euro20c)//10
euro5c =(amount-200*euro2-100*euro1-50*euro50c-20*euro20c-10*euro10c)//5
euro2c =(amount-200*euro2-100*euro1-50*euro50c-20*euro20c-10*euro10c-5*euro5c)//2
euro1c =(amount-200*euro2-100*euro1-50*euro50c-20*euro20c-10*euro10c-5*euro5c-2*euro2c)//1

print("2-euros:", euro2)
print("1-euros:", euro1)
print("50c-euros:", euro50c)
print("20c-euros:", euro20c)
print("10c-euros:", euro10c)
print("5c-euros:", euro5c)
print("2c-euros:", euro2c)
print("1c-euros:", euro1c)