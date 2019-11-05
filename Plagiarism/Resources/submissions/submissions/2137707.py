# write your code here

integer = int(input("input integer: "))
i = 0
amount = 0

while i+1 <= len(str(integer)):
    char_integer = str(integer)
    char_integer = char_integer[i]
    if int(char_integer) % 2 == 0:
        amount += 1
    i += 1
    
print(amount)