euro1 = int(input("Type in how many 1eurocent coins you have"))
euro2 = int(input("Type in how many 2eurocent coins you have"))
euro5 = int(input("Type in how many 5eurocent coins you have"))
euro10 = int(input("Type in how many 10eurocent coins you have"))
euro20 = int(input("Type in how many 20eurocent coins you have"))

t1 = euro1 * 1
t2 = euro2 * 2
t5 = euro5 * 5
t10 = euro10 * 10
t20 = euro20 * 20
totaal = t1 + t2 + t5 + t10 + t20 

print("You have ", totaal / 100, " euro!")
