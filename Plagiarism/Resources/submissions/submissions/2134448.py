oneCent = float(input())
twoCent = float(input())
fiveCent = float(input())
tenCent = float(input())
twentyCent = float(input())

sum = (oneCent * 0.01) + (twoCent * 0.02) + (fiveCent * 0.05) + (tenCent * 0.10) + (twentyCent * 0.20)

print("You have " + str(format(sum, '.2f')) + " euro!")