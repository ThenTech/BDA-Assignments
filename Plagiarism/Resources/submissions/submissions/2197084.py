def convert_to_uppercase(s):
    lengthe = len(s)
    new =""
    s = s.lower()
    for i in range(lengthe -1):
        if s[i] == " ":
            new += " "
        else:
            new += chr(ord(s[i]) - 32)
    return new
print(convert_to_uppercase("A simple example string!"))