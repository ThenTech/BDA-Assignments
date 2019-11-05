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

        elif string == "X" or string == " ":
            string = "0"
    return str(string)