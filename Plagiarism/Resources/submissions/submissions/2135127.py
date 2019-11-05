import string

alphabet = string.ascii_lowercase
s = input("")

count = 0

while count < 26:
    print(str(alphabet[count]) + ": " + str(s.count(alphabet[count])))
    count += 1