# write your code here

number = input("Geef een getal in: ")
count = 0

for i in range(0, len(number)):
    if (int(number[i]) % 2) == 0:
        count += 1

print(count)
