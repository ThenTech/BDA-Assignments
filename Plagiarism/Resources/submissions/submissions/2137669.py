# write your code here

a_string = input("Give me a string: ")
str_len = len(a_string)

for index in range(26):
    # ord / chr value of 'a' is 97
    # a has an ORDER value of 97 or is the 97 character
    # b: 98, c: 99, ...
    current_letter = 97 + index

    # Holds the amount of the current letter in the string 
    amount = 0
    for x in range(str_len):
        # Checks when the current letter == the current letter of the given string 
        # This will add 1 to amount every time a letter in the string is a current letter
        if current_letter == ord( a_string[x] ):
            amount += 1

    print(chr(current_letter), ": ", amount, sep="")