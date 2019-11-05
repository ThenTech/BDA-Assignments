number = input("Give a number: ")
while number < '1':
    number = input("Give a number: ")
num_len = len(number)

count = 0
for i in range(num_len):
    if int(number[i]) % 2 == 0:
        count += 1
print(count)
