n1 = int(input("first number: "))
n2 = int(input("second number: "))
if n2 == 1:
    Final = 1
else:
    Final = (n1/n2) * ((n1 - 1) / (n2 - 1)) * ((n1 - n2 + 1) / 1)
print(round(Final))
