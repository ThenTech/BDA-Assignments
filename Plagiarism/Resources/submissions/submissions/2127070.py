one = float(input("how many one cents? "))
two = float(input("how many two cents? "))
five = float(input("How many five cents? "))
ten = float(input("how many ten cents? "))
twenty = float(input("how many twenty cents? "))
sum = one + 2 * two + 5 * five + 10 * ten + 20 * twenty
sum = sum/100
sum = str(sum)
print("You have " + sum + "euro!")