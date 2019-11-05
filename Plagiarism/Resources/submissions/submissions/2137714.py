number = input()
i = 0
amount = 0
while i < len(number):
    if int(number[i]) % 2 == 0:
        amount += 1
    else:
        continue
print(amount)