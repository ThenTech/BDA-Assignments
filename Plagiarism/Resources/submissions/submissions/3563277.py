string = input("give a string: ")
if (len(string)) == 0:
    print()
else:
    split_string = " "
    string += "!"

    for i in range(len(string) - 1):
        if string[i] >= "A" and string[i] <= "z":
            split_string += string[i]
        elif string[i] != " ":
            split_string += " "
        elif string[i] == " ":
            split_string += " "

    split_string += " "


    split_string_2 = ""

    for i in range(1,len(split_string)-1):
        if split_string[i] == " " and split_string[i + 1] == " ":
            split_string_2 += ""
        else:
            split_string_2 += split_string[i]

    split_string_2 += " "
    split_string_2 += " "


    index = 0

    for i in range(len(split_string_2)-1):
        if split_string_2[i] == " ":
            print(split_string_2[index:i], len(split_string_2[index:i]))
            index = i + 1
