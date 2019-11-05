ones = input("amount of 1 cents: ")
twos = input("amount of 2 cents: ")
fives = input("amount of 5 cents: ")
tens = input("amount of 10 cents: ")
twen = input("amount of 20 cents: ")
c_ones = float(ones) * 0.01
c_twos = float(twos) * 0.02
c_fives = float(fives) * 0.05
c_tens = float(tens) * 0.10
c_twen = float(twen) * 0.20
total = c_ones + c_twos + c_fives + c_tens + c_twen
x = int(total)
y = int((total - int(total))*10)
z = int(((total - int(total) - (y/10))*100 ))


print("You have ", x, ".", y, z, " euro!", sep="")