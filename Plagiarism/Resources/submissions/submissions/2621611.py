def encode(string):
    for i in range(len(string)):
        if i == 0 and len(string) > 1:
            count = 0
            if string[i + 1] == "X":
                count += 1
            if count == 0:
                print("0", end="")
            else:
                print(count, end="")

        elif i == len(string)-1 and len(string) > 1:
            count = 0
            if string[i - 1] == "X":
                count += 1
            if count == 0:
                print("0", end="")
            else:
                print(count, end ="")

        elif len(string) > 1:
            count = 0
            if string[i-1] == "X":
                count += 1
            if string[i+1] == "X":
                count += 1
            if count == 0:
                print("0", end="")
            else:
                print(count, end="")

        elif string == "x" or string == " ":
            string = "0"
            

def decode(string):
    for i in range(len(string)):
        if string[i] == "2":
            string = string[:i-1] + "X X" + string[i+2:]
    for i in range(len(string)):
        if i == 0:
            if string[i] == "1":
                string = " X" + string[2:]
        elif i == len(string)-1:
            if string[i] == "1":
                string = string[:len(string)-3] + "X "
        elif string[i] == "1":
            string = string[:i]+ " X" + string[i+2:]

    return string