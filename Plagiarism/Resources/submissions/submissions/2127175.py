# write your code here
totalEurocents = int(input())

twoEuros = totalEurocents // 100 // 2
oneEuros = totalEurocents // 100 % 2
fiftyEurocents = totalEurocents % 100 // 50
twentyEurocents = totalEurocents % 100 % 50 // 20
tenEurocents = totalEurocents % 100 % 50 % 20 // 10
fiveEurocents = totalEurocents % 100 % 10 // 5
twoEurocents = totalEurocents % 100 % 5 // 2
oneEurocents = totalEurocents % 100 % 5 % 2

print("2-euros:" , twoEuros)
print("1-euros:" , oneEuros)
print("50c-euros:" , fiftyEurocents)
print("20c-euros:" , twentyEurocents)
print("10c-euros:" , tenEurocents)
print("5c-euros:" , fiveEurocents)
print("2c-euros:" , twoEurocents)
print("1c-euros:" , oneEurocents)