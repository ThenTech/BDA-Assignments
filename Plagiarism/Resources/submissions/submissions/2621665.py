def encode(string):
    new_string =""
    for i in range(len(string)):
        if i == 0 and len(string) > 1:
            count = 0
            if string[i + 1] == "X":
                count += 1
            if count == 0:
                new_string += "0"
            else:
                new_string += str(count)

        elif i == len(string)-1 and len(string) > 1:
            count = 0
            if string[i - 1] == "X":
                count += 1
            if count == 0:
                new_string += "0"
            else:
                new_string += str(count)

        elif len(string) > 1:
            count = 0
            if string[i-1] == "X":
                count += 1
            if string[i+1] == "X":
                count += 1
            if count == 0:
                new_string += "0"
            else:
                new_string += str(count)

        elif string == "X" or string == " ":
            string = "0"
    return string