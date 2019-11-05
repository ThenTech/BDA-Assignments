number = input()
pos = 0
amount = 0
while pos < len(number):
    if int(number[pos]) % 2 == 0:
        amount += 1
    pos += 1
print(amount)