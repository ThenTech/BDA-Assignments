import string

alphabet = string.ascii_lowercase
s = input("")

count = 0

while count < 26:
    print(alphabet[count] + ": " + s.count(alphabet[count]))
    count += 1