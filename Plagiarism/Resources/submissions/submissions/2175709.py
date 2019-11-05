alphabet = "abcdefghijklmnopqrstuvwxyz"
stringinput = input("Give a string: ")
timeschar = 0
bool = False


for char in alphabet:
    timeschar = 0
    for i in range(0, len(stringinput)):
        if (char == stringinput[i]):
            timeschar = timeschar + 1
    print(char, timeschar, sep = ": ")