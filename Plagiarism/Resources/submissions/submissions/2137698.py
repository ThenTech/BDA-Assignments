# write your code here

integer = int(input("input integer: "))
i = 0
amount = 0

while i+1 <= len(str(integer)):
    if int(str(integer[i])) % 2 == 0:
        amount += 1
    i += 1
    
print(amount)