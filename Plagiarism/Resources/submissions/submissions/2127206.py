# write your code here
one=int(input("Put in the amount of 1 eurocent coins you have."))
two=int(input("Put in the amount of 2 eurocent coins you have."))
five=int(input("Put in the amount of 5 eurocent coins you have."))
ten=int(input("Put in the amount of 10 eurocent coins you have."))
twenty=int(input("Put in the amount of 20 eurocent coins you have."))
amount=float((1.0*one+2.0*two+5.0*five+10*ten+20*twenty)/100)
print("You have", amount, "euro!")