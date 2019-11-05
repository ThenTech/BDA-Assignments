number = input("Give a number: ")

count_even = 0

for j in range(0, len(number)):
    convert = int(number[j])
    if(convert % 2 == 0):
        count_even += 1

print(count_even)