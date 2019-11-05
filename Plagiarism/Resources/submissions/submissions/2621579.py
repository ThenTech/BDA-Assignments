def encode(string):
    for i in range(len(string)):
        if i == 0:
            count = 0
            if string[i + 1] == "X":
                count += 1
            if count == 0:
                print(" ", end="")
            else:
                print(count, end="")

        elif i == len(string)-1:
            count = 0
            if string[i - 1] == "X":
                count += 1
            if count == 0:
                print(" ", end="")
            else:
                print(count, end ="")

        else:
            count = 0
            if string[i-1] == "X":
                count += 1
            if string[i+1] == "X":
                count += 1
            if count == 0:
                print(" ", end="")
            else:
                print(count, end ="")

def decode(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] == "2":
            string = string[:i-1] + "X X" + string[i+2:]
    for i in range(len(string)):
        if i == 0:
            if string[i] == "1":
                string = " X" + string[2:]
        elif i == len(string)-1:
            if string[i] == "1":
                string = string[:len(string)-2] + " "
        elif string[i] == "1":
            string = string[:i]+ " X" + string[i+2:]

    return string