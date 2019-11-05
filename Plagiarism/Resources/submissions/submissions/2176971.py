# write your code here
numbers = input("Give me some numbers:")
even = 0

for i in numbers:
    if int(i) % 2 == 0:
        even = even + 1

print(even)