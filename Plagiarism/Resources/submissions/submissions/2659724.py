given_string = input()
given_string = given_string + "  "
count = 0
for i in range(len(given_string)):
    if 97 <= ord(given_string[i]) <= 122 or 65 <= ord(given_string[i]) <= 90:
        print(given_string[i], end="")
        count += 1
        if (i < (len(given_string) - 2)) and given_string[i+1] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print(" ",count, sep="")
            count = 0
    else:
        count = 0
        