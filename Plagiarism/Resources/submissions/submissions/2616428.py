def convert_to_uppercase(string):
    optel = ord("A") - ord("a")
    string2 = ""
    for i in string:
        if "a" <= i <= "z":
            cijfer = ord(i)
            cijfer += optel
            letter = chr(cijfer)
            string2 += letter
        else:
            string2 += i
    return string2