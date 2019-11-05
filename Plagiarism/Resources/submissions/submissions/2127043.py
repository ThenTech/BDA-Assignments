# write your code here
eeneurocent = int(input(" how many 1 eurocents? "))
tweeeurocent = int(input(" how many 2 eurocents? ")) * 2
vijfeurocent = int(input(" how many 5 eurocents? ")) * 5
tieneurocent = int(input(" how many 10 eurocents? ")) * 10
twintigeurocent = int(input(" how many 20 eurocent? ")) * 20

total = round(float(eeneurocent + tweeeurocent + vijfeurocent + tieneurocent + twintigeurocent) / 100, 2)

print("You have ", total, " euro!", sep="")
