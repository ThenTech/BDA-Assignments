def convert_to_uppercase(s):
    lengthe = len(s)
    new =""
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwqxyz"
    for i in range(lengthe):
        if s[i] in alphabet:
            if s[i] == " ":
                new += " "
            else:
                new += chr(ord(s[i]) - 32)
        else:
            new+= s[i]
    return new
print(convert_to_uppercase("A simple example string!"))