# write your code here

int_value = input("Give me a integer: ")
counter = 0

for letter in int_value:
    if int(letter) % 2 == 0:
        counter += 1
print(counter)