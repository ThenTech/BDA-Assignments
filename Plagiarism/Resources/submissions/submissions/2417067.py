s = str(input("string:"))
alfabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alfabet:
    waarde = 0
    for i in range(len(s)-1):
        if s[i] == letter:
            waarde += 1
    print(letter + ":", waarde)