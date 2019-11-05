s = input("give string: ")
alfabet = "abcdefghijklmnopqrstuvwxyz"
count = 0
for letter in alfabet:
    count = 0
    for i in s:
        if letter == i:
            count += 1
        else:
            count = count

    print(letter +":", count)