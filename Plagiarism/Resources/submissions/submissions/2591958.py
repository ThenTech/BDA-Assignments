alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
string = input("Enter some shit plz")
string_and_length = ""
count = 0
for i in range(len(string) - 1):
    if string[i] in alphabet:
        if (i + 1) == (len(string) - 1):
            if string[i + 1] in alphabet:
                string_and_length += string[i+1]
                count += 1
            count += 1
            string_and_length += string[i]
            print(string_and_length + " " + str(count))
        else:
            if string[i + 1] in alphabet:
                string_and_length += string[i]
                count += 1
            if string[i + 1] not in alphabet:
                count += 1
                string_and_length += (string[i] + " " + str(count))
                print(string_and_length)
                count = 0
                string_and_length = ""

