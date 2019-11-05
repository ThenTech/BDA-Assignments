aantal1 = float(input("Hoeveel keer 1 eurocent heeft u? "))
aantal2 = float(input("Hoeveel keer 2 eurocent heeft u? "))
aantal5 = float(input("Hoeveel keer 5 eurocent heeft u? "))
aantal10 = float(input("Hoeveel keer 10 eurocent heeft u? "))
aantal20= float(input("Hoeveel keer 20 eurocent heeft u? "))
som = aantal1*0.01 + aantal2*0.02 + aantal5*0.05 + aantal10*0.1 + aantal20*0.2

print("You have ", som,"euro!")