ones = input("amount of 1 cents: ")
twos = input("amount of 2 cents: ")
fives = input("amount of 5 cents: ")
tens = input("amount of 10 cents: ")
twen = input("amount of 20 cents: ")
c_ones = int(ones) * 0.01
c_twos = int(twos) * 0.02
c_fives = int(fives) * 0.05
c_tens = int(tens) * 0.10
c_twen = int(twen) * 0.20
total = c_ones + c_twos + c_fives + c_tens + c_twen
x = int(total)
y = (total - int(total))// 0.10
z = (total - int(total) - (y*0.1)) // 0.01


print("You have ", x, ".", y, z, " euro!", sep="")